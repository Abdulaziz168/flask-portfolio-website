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
    
    print("\n" + "="*60)
    print("🚀 Portfolio Website Starting...")
    print("="*60)
    print("📍 Local URL: http://127.0.0.1:5000")
    print("👤 Admin Panel: http://127.0.0.1:5000/admin/login")
    print("🔐 Default Credentials: admin / admin123")
    print("="*60 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)
