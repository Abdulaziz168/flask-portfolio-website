"""
Portfolio Website - Main Entry Point
Run this file to start the Flask application
"""
from app import create_app, db
from app.models import AdminUser, Project, BlogPost, ContactMessage

app = create_app()


@app.shell_context_processor
def make_shell_context():
    """Make database models available in Flask shell"""
    return {
        'db': db,
        'AdminUser': AdminUser,
        'Project': Project,
        'BlogPost': BlogPost,
        'ContactMessage': ContactMessage
    }


if __name__ == '__main__':
    with app.app_context():
        # Create all database tables
        db.create_all()
        
        # Create default admin user if not exists
        admin = AdminUser.query.filter_by(username='admin').first()
        if not admin:
            admin = AdminUser(username='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("✓ Default admin user created (username: admin, password: admin123)")
        
        print("✓ Database initialized successfully")
        
        # Check if there's any data
        project_count = Project.query.count()
        blog_count = BlogPost.query.count()
        
        if project_count == 0 and blog_count == 0:
            print("\n" + "="*60)
            print("⚠️  NOTE: Database is empty!")
            print("="*60)
            print("To add sample data, run:")
            print("  python init_data.py")
            print("="*60 + "\n")
    
    print("\n" + "="*60)
    print("🚀 Portfolio Website Starting...")
    print("="*60)
    print("📍 Local URL: http://127.0.0.1:5000")
    print("👤 Admin Panel: http://127.0.0.1:5000/admin/login")
    print("🔐 Default Credentials: admin / admin123")
    print("="*60 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)
