"""
Application Routes and Blueprints
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Project, BlogPost, ContactMessage, AdminUser
from app.forms import ContactForm, LoginForm, ProjectForm, BlogPostForm
from functools import wraps
from sqlalchemy import or_, desc

# Main blueprint for public pages
main_bp = Blueprint('main', __name__)

# Admin blueprint for admin panel
admin_bp = Blueprint('admin', __name__)


def login_required(f):
    """Decorator to require admin login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            flash('Please login to access the admin panel', 'warning')
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function


# ============================================
# PUBLIC ROUTES
# ============================================

@main_bp.route('/')
def index():
    """Home page"""
    # Get latest projects for home page
    latest_projects = Project.query.order_by(desc(Project.date)).limit(6).all()
    return render_template('index.html', projects=latest_projects)


@main_bp.route('/about')
def about():
    """About page"""
    return render_template('about.html')


@main_bp.route('/projects')
def projects():
    """Projects listing page with search and filter"""
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category', '')
    search = request.args.get('search', '')
    per_page = 9
    
    # Build query
    query = Project.query
    
    # Apply category filter
    if category:
        query = query.filter_by(category=category)
    
    # Apply search filter
    if search:
        search_term = f'%{search}%'
        query = query.filter(
            or_(
                Project.title.ilike(search_term),
                Project.description.ilike(search_term),
                Project.technology_stack.ilike(search_term)
            )
        )
    
    # Paginate results
    projects = query.order_by(desc(Project.date)).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    # Get all categories for filter
    categories = db.session.query(Project.category).distinct().all()
    categories = [c[0] for c in categories]
    
    return render_template('projects.html', 
                         projects=projects,
                         categories=categories,
                         current_category=category,
                         search_query=search)


@main_bp.route('/project/<slug>')
def project_detail(slug):
    """Project detail page"""
    project = Project.query.filter_by(slug=slug).first_or_404()
    
    # Get related projects (same category, exclude current)
    related_projects = Project.query.filter(
        Project.category == project.category,
        Project.id != project.id
    ).limit(3).all()
    
    return render_template('project_detail.html', 
                         project=project,
                         related_projects=related_projects)


@main_bp.route('/services')
def services():
    """Services page"""
    return render_template('services.html')


@main_bp.route('/blog')
def blog():
    """Blog listing page"""
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category', '')
    search = request.args.get('search', '')
    per_page = 6
    
    # Build query
    query = BlogPost.query
    
    # Apply category filter
    if category:
        query = query.filter_by(category=category)
    
    # Apply search filter
    if search:
        search_term = f'%{search}%'
        query = query.filter(
            or_(
                BlogPost.title.ilike(search_term),
                BlogPost.content.ilike(search_term),
                BlogPost.tags.ilike(search_term)
            )
        )
    
    # Paginate results
    posts = query.order_by(desc(BlogPost.date)).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    # Get latest posts for sidebar
    latest_posts = BlogPost.query.order_by(desc(BlogPost.date)).limit(5).all()
    
    # Get all categories for filter
    categories = db.session.query(BlogPost.category).distinct().all()
    categories = [c[0] for c in categories]
    
    return render_template('blog.html',
                         posts=posts,
                         latest_posts=latest_posts,
                         categories=categories,
                         current_category=category,
                         search_query=search)


@main_bp.route('/blog/<slug>')
def blog_detail(slug):
    """Blog post detail page"""
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    
    # Get latest posts for sidebar
    latest_posts = BlogPost.query.order_by(desc(BlogPost.date)).limit(5).all()
    
    # Get related posts (same category, exclude current)
    related_posts = BlogPost.query.filter(
        BlogPost.category == post.category,
        BlogPost.id != post.id
    ).limit(3).all()
    
    return render_template('blog_detail.html',
                         post=post,
                         latest_posts=latest_posts,
                         related_posts=related_posts)


@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form"""
    form = ContactForm()
    
    if form.validate_on_submit():
        # Create new contact message
        message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        
        db.session.add(message)
        db.session.commit()
        
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('main.contact'))
    
    return render_template('contact.html', form=form)


# ============================================
# ADMIN ROUTES
# ============================================

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login page"""
    if 'admin_logged_in' in session:
        return redirect(url_for('admin.dashboard'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        admin = AdminUser.query.filter_by(username=form.username.data).first()
        
        if admin and admin.check_password(form.password.data):
            session['admin_logged_in'] = True
            session['admin_username'] = admin.username
            flash('Login successful!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('admin/login.html', form=form)


@admin_bp.route('/logout')
def logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    session.pop('admin_username', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('admin.login'))


@admin_bp.route('/dashboard')
@login_required
def dashboard():
    """Admin dashboard"""
    # Get statistics
    total_projects = Project.query.count()
    total_blog_posts = BlogPost.query.count()
    total_messages = ContactMessage.query.count()
    unread_messages = ContactMessage.query.filter_by(is_read=False).count()
    
    # Get recent items
    recent_projects = Project.query.order_by(desc(Project.created_at)).limit(5).all()
    recent_posts = BlogPost.query.order_by(desc(BlogPost.created_at)).limit(5).all()
    recent_messages = ContactMessage.query.order_by(desc(ContactMessage.date)).limit(5).all()
    
    return render_template('admin/dashboard.html',
                         total_projects=total_projects,
                         total_blog_posts=total_blog_posts,
                         total_messages=total_messages,
                         unread_messages=unread_messages,
                         recent_projects=recent_projects,
                         recent_posts=recent_posts,
                         recent_messages=recent_messages)


# ============================================
# ADMIN - PROJECT MANAGEMENT
# ============================================

@admin_bp.route('/projects')
@login_required
def manage_projects():
    """List all projects"""
    page = request.args.get('page', 1, type=int)
    projects = Project.query.order_by(desc(Project.created_at)).paginate(
        page=page, per_page=10, error_out=False
    )
    return render_template('admin/projects.html', projects=projects)


@admin_bp.route('/project/create', methods=['GET', 'POST'])
@login_required
def create_project():
    """Create new project"""
    form = ProjectForm()
    
    if form.validate_on_submit():
        project = Project(
            title=form.title.data,
            slug=form.slug.data,
            description=form.description.data,
            image=form.image.data,
            technology_stack=form.technology_stack.data,
            github_url=form.github_url.data,
            live_demo_url=form.live_demo_url.data,
            category=form.category.data,
            features=form.features.data
        )
        
        db.session.add(project)
        db.session.commit()
        
        flash('Project created successfully!', 'success')
        return redirect(url_for('admin.manage_projects'))
    
    return render_template('admin/project_form.html', form=form, title='Create Project')


@admin_bp.route('/project/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    """Edit existing project"""
    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)
    
    if form.validate_on_submit():
        project.title = form.title.data
        project.slug = form.slug.data
        project.description = form.description.data
        project.image = form.image.data
        project.technology_stack = form.technology_stack.data
        project.github_url = form.github_url.data
        project.live_demo_url = form.live_demo_url.data
        project.category = form.category.data
        project.features = form.features.data
        
        db.session.commit()
        
        flash('Project updated successfully!', 'success')
        return redirect(url_for('admin.manage_projects'))
    
    return render_template('admin/project_form.html', form=form, title='Edit Project', project=project)


@admin_bp.route('/project/delete/<int:id>')
@login_required
def delete_project(id):
    """Delete project"""
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    
    flash('Project deleted successfully!', 'success')
    return redirect(url_for('admin.manage_projects'))


# ============================================
# ADMIN - BLOG MANAGEMENT
# ============================================

@admin_bp.route('/blog')
@login_required
def manage_blog():
    """List all blog posts"""
    page = request.args.get('page', 1, type=int)
    posts = BlogPost.query.order_by(desc(BlogPost.created_at)).paginate(
        page=page, per_page=10, error_out=False
    )
    return render_template('admin/blog.html', posts=posts)


@admin_bp.route('/blog/create', methods=['GET', 'POST'])
@login_required
def create_blog():
    """Create new blog post"""
    form = BlogPostForm()
    
    if form.validate_on_submit():
        post = BlogPost(
            title=form.title.data,
            slug=form.slug.data,
            content=form.content.data,
            image=form.image.data,
            category=form.category.data,
            tags=form.tags.data,
            author=form.author.data
        )
        
        db.session.add(post)
        db.session.commit()
        
        flash('Blog post created successfully!', 'success')
        return redirect(url_for('admin.manage_blog'))
    
    return render_template('admin/blog_form.html', form=form, title='Create Blog Post')


@admin_bp.route('/blog/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_blog(id):
    """Edit existing blog post"""
    post = BlogPost.query.get_or_404(id)
    form = BlogPostForm(obj=post)
    
    if form.validate_on_submit():
        post.title = form.title.data
        post.slug = form.slug.data
        post.content = form.content.data
        post.image = form.image.data
        post.category = form.category.data
        post.tags = form.tags.data
        post.author = form.author.data
        
        db.session.commit()
        
        flash('Blog post updated successfully!', 'success')
        return redirect(url_for('admin.manage_blog'))
    
    return render_template('admin/blog_form.html', form=form, title='Edit Blog Post', post=post)


@admin_bp.route('/blog/delete/<int:id>')
@login_required
def delete_blog(id):
    """Delete blog post"""
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    
    flash('Blog post deleted successfully!', 'success')
    return redirect(url_for('admin.manage_blog'))


# ============================================
# ADMIN - MESSAGE MANAGEMENT
# ============================================

@admin_bp.route('/messages')
@login_required
def view_messages():
    """View all contact messages"""
    page = request.args.get('page', 1, type=int)
    messages = ContactMessage.query.order_by(desc(ContactMessage.date)).paginate(
        page=page, per_page=10, error_out=False
    )
    return render_template('admin/messages.html', messages=messages)


@admin_bp.route('/message/<int:id>')
@login_required
def view_message(id):
    """View single message and mark as read"""
    message = ContactMessage.query.get_or_404(id)
    
    if not message.is_read:
        message.is_read = True
        db.session.commit()
    
    return render_template('admin/message_detail.html', message=message)


@admin_bp.route('/message/delete/<int:id>')
@login_required
def delete_message(id):
    """Delete message"""
    message = ContactMessage.query.get_or_404(id)
    db.session.delete(message)
    db.session.commit()
    
    flash('Message deleted successfully!', 'success')
    return redirect(url_for('admin.view_messages'))
