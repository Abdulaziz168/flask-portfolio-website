"""
Database Models
"""
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class AdminUser(db.Model):
    """Admin user model for authentication"""
    __tablename__ = 'admin_users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        """Hash and set password"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verify password"""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<AdminUser {self.username}>'


class Project(db.Model):
    """Project model for portfolio projects"""
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(300), nullable=True)
    technology_stack = db.Column(db.String(500), nullable=False)  # Comma-separated
    github_url = db.Column(db.String(300), nullable=True)
    live_demo_url = db.Column(db.String(300), nullable=True)
    category = db.Column(db.String(100), nullable=False)
    features = db.Column(db.Text, nullable=True)  # Line-separated features
    date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Project {self.title}>'
    
    @property
    def tech_list(self):
        """Return technology stack as list"""
        return [tech.strip() for tech in self.technology_stack.split(',') if tech.strip()]
    
    @property
    def feature_list(self):
        """Return features as list"""
        if self.features:
            return [f.strip() for f in self.features.split('\n') if f.strip()]
        return []


class BlogPost(db.Model):
    """Blog post model"""
    __tablename__ = 'blog_posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(300), nullable=True)
    category = db.Column(db.String(100), nullable=False)
    tags = db.Column(db.String(300), nullable=True)  # Comma-separated
    author = db.Column(db.String(100), default='Admin')
    date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<BlogPost {self.title}>'
    
    @property
    def tag_list(self):
        """Return tags as list"""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
        return []
    
    @property
    def excerpt(self):
        """Return first 200 characters of content"""
        return self.content[:200] + '...' if len(self.content) > 200 else self.content


class ContactMessage(db.Model):
    """Contact message model"""
    __tablename__ = 'contact_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<ContactMessage from {self.name}>'
