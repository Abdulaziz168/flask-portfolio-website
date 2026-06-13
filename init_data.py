"""
Initialize Database with Sample Data
Run this script to populate the database with sample projects and blog posts
"""
from app import create_app, db
from app.models import Project, BlogPost, AdminUser
from datetime import datetime, timedelta

app = create_app()

def init_sample_data():
    """Initialize database with sample data"""
    with app.app_context():
        # Create all database tables first
        print("Creating database tables...")
        db.create_all()
        
        # Clear existing data (optional)
        print("Clearing existing data...")
        try:
            Project.query.delete()
            BlogPost.query.delete()
        except Exception as e:
            print(f"Note: {e}")
            print("Tables are empty or being created for the first time.")
        
        # Sample Projects
        print("Creating sample projects...")
        projects = [
            {
                'title': 'E-Commerce Platform',
                'slug': 'ecommerce-platform',
                'description': 'A full-featured e-commerce platform built with Flask and SQLAlchemy. Features include user authentication, product management, shopping cart, payment integration, and admin dashboard.',
                'image': 'https://via.placeholder.com/800x500/667eea/ffffff?text=E-Commerce+Platform',
                'technology_stack': 'Python, Flask, SQLAlchemy, Bootstrap, Stripe API, PostgreSQL',
                'github_url': 'https://github.com/yourusername/ecommerce-platform',
                'live_demo_url': 'https://demo.ecommerce.com',
                'category': 'Web Application',
                'features': '''User authentication and authorization
Product catalog with search and filters
Shopping cart and wishlist
Secure payment processing with Stripe
Order tracking and management
Admin dashboard for inventory management
Responsive design for all devices'''
            },
            {
                'title': 'Task Management System',
                'slug': 'task-management-system',
                'description': 'A collaborative task management system with real-time updates. Teams can create projects, assign tasks, set deadlines, and track progress efficiently.',
                'image': 'https://via.placeholder.com/800x500/8b5cf6/ffffff?text=Task+Manager',
                'technology_stack': 'Flask, WebSockets, SQLite, JavaScript, Chart.js',
                'github_url': 'https://github.com/yourusername/task-manager',
                'live_demo_url': 'https://demo.taskmanager.com',
                'category': 'Productivity',
                'features': '''Real-time collaboration
Project and task organization
Team member management
Progress tracking with visual charts
Deadline notifications
File attachments
Activity timeline'''
            },
            {
                'title': 'Weather Dashboard',
                'slug': 'weather-dashboard',
                'description': 'An interactive weather dashboard that displays current weather, forecasts, and historical data. Features beautiful visualizations and location-based weather information.',
                'image': 'https://via.placeholder.com/800x500/10b981/ffffff?text=Weather+Dashboard',
                'technology_stack': 'Python, Flask, OpenWeather API, Chart.js, Bootstrap',
                'github_url': 'https://github.com/yourusername/weather-dashboard',
                'live_demo_url': 'https://demo.weather.com',
                'category': 'API Integration',
                'features': '''Current weather conditions
7-day forecast
Hourly predictions
Location-based weather
Interactive maps
Historical data visualization
Multiple location support'''
            },
            {
                'title': 'Blog CMS',
                'slug': 'blog-cms',
                'description': 'A content management system designed specifically for bloggers. Rich text editor, SEO optimization, and powerful admin features make content creation effortless.',
                'image': 'https://via.placeholder.com/800x500/f59e0b/ffffff?text=Blog+CMS',
                'technology_stack': 'Flask, TinyMCE, SQLAlchemy, Redis, Markdown',
                'github_url': 'https://github.com/yourusername/blog-cms',
                'live_demo_url': None,
                'category': 'Content Management',
                'features': '''Rich text editor with markdown support
SEO optimization tools
Category and tag management
Comment system with moderation
Image upload and management
Draft and scheduled posts
User roles and permissions'''
            },
            {
                'title': 'Telegram Bot Framework',
                'slug': 'telegram-bot-framework',
                'description': 'A comprehensive framework for building Telegram bots with Python. Includes built-in commands, inline keyboards, payment processing, and database integration.',
                'image': 'https://via.placeholder.com/800x500/06b6d4/ffffff?text=Telegram+Bot',
                'technology_stack': 'Python, python-telegram-bot, SQLite, Flask',
                'github_url': 'https://github.com/yourusername/telegram-bot-framework',
                'live_demo_url': None,
                'category': 'Automation',
                'features': '''Easy bot configuration
Built-in command handlers
Inline keyboard support
Payment integration
User management
Database integration
Webhook support
Admin panel'''
            },
            {
                'title': 'Portfolio Generator',
                'slug': 'portfolio-generator',
                'description': 'An automated portfolio website generator that creates beautiful, responsive portfolio sites from templates. Users can customize themes, add projects, and deploy instantly.',
                'image': 'https://via.placeholder.com/800x500/ec4899/ffffff?text=Portfolio+Generator',
                'technology_stack': 'Flask, Jinja2, Bootstrap, SQLite, HTML/CSS',
                'github_url': 'https://github.com/yourusername/portfolio-generator',
                'live_demo_url': 'https://demo.portfoliogen.com',
                'category': 'Web Application',
                'features': '''Multiple templates
Drag-and-drop interface
Project showcase
Blog integration
Contact forms
SEO optimization
One-click deployment'''
            }
        ]
        
        for project_data in projects:
            project = Project(**project_data)
            db.session.add(project)
        
        # Sample Blog Posts
        print("Creating sample blog posts...")
        blog_posts = [
            {
                'title': 'Getting Started with Flask Web Development',
                'slug': 'getting-started-flask',
                'content': '''Flask is a lightweight and flexible Python web framework that makes it easy to build web applications. In this comprehensive guide, we'll explore the fundamentals of Flask development.

Flask follows a minimalist philosophy, providing the essentials while allowing developers to choose their tools and libraries. This flexibility makes it perfect for projects of all sizes.

Key Features of Flask:
- Simple and intuitive API
- Built-in development server and debugger
- RESTful request dispatching
- Jinja2 templating
- Secure cookie support
- WSGI compliance
- Extensive documentation

Whether you're building a small website or a complex web application, Flask provides the tools you need to succeed. Its lightweight nature and extensive ecosystem make it an excellent choice for both beginners and experienced developers.

In upcoming tutorials, we'll dive deeper into Flask blueprints, database integration, authentication, and deployment strategies.''',
                'image': 'https://via.placeholder.com/800x500/667eea/ffffff?text=Flask+Tutorial',
                'category': 'Tutorial',
                'tags': 'python, flask, web-development, tutorial',
                'author': 'Admin',
                'date': datetime.utcnow() - timedelta(days=5)
            },
            {
                'title': 'Building RESTful APIs with Flask',
                'slug': 'building-restful-apis-flask',
                'content': '''RESTful APIs are the backbone of modern web applications. Flask makes it incredibly easy to build robust, scalable APIs that can power your applications.

In this post, we'll explore best practices for API development, including proper HTTP methods, status codes, authentication, and error handling.

Essential API Concepts:
- Resource-based URLs
- HTTP methods (GET, POST, PUT, DELETE)
- Status codes and error handling
- Authentication and authorization
- Rate limiting
- Versioning
- Documentation

Flask-RESTful and Flask-RESTX are excellent extensions that simplify API development even further. They provide decorators, request parsing, and automatic Swagger documentation.

We'll also cover testing your APIs, securing endpoints, and optimizing performance for production environments.''',
                'image': 'https://via.placeholder.com/800x500/8b5cf6/ffffff?text=REST+API',
                'category': 'Tutorial',
                'tags': 'flask, api, rest, backend',
                'author': 'Admin',
                'date': datetime.utcnow() - timedelta(days=10)
            },
            {
                'title': 'Database Management with SQLAlchemy',
                'slug': 'database-management-sqlalchemy',
                'content': '''SQLAlchemy is the premier SQL toolkit for Python, providing a full suite of enterprise-level persistence patterns. When combined with Flask, it becomes an incredibly powerful tool for database management.

Understanding Object-Relational Mapping (ORM):
SQLAlchemy's ORM allows you to work with database records as Python objects, making your code more intuitive and maintainable.

Key concepts include:
- Models and schemas
- Relationships (one-to-many, many-to-many)
- Queries and filtering
- Migrations with Flask-Migrate
- Performance optimization
- Connection pooling

Whether you're working with SQLite for development or PostgreSQL for production, SQLAlchemy provides a consistent interface that scales with your application.

We'll explore advanced topics like lazy loading, eager loading, query optimization, and handling complex relationships in future posts.''',
                'image': 'https://via.placeholder.com/800x500/10b981/ffffff?text=SQLAlchemy',
                'category': 'Database',
                'tags': 'sqlalchemy, database, orm, flask',
                'author': 'Admin',
                'date': datetime.utcnow() - timedelta(days=15)
            },
            {
                'title': 'Deploying Flask Applications to Production',
                'slug': 'deploying-flask-production',
                'content': '''Moving your Flask application from development to production requires careful planning and consideration of various factors including performance, security, and scalability.

Production Deployment Checklist:
- Use a production-ready WSGI server (Gunicorn, uWSGI)
- Configure environment variables
- Set up a reverse proxy (Nginx, Apache)
- Enable HTTPS with SSL certificates
- Configure logging and monitoring
- Implement caching strategies
- Set up automated backups
- Use a process manager (systemd, Supervisor)

Popular deployment platforms include:
- Heroku (easy, managed)
- DigitalOcean (flexible, affordable)
- AWS (scalable, feature-rich)
- Google Cloud Platform
- PythonAnywhere

Each platform has its pros and cons. We'll walk through deployment on multiple platforms and discuss best practices for maintaining production applications.''',
                'image': 'https://via.placeholder.com/800x500/f59e0b/ffffff?text=Deployment',
                'category': 'DevOps',
                'tags': 'deployment, production, devops, flask',
                'author': 'Admin',
                'date': datetime.utcnow() - timedelta(days=20)
            },
            {
                'title': '10 Tips for Writing Clean Python Code',
                'slug': 'clean-python-code-tips',
                'content': '''Writing clean, maintainable code is essential for any professional developer. Here are ten practical tips to improve your Python code quality.

1. Follow PEP 8 Style Guidelines
Python has official style guidelines that make code consistent and readable across projects.

2. Use Meaningful Variable Names
Choose descriptive names that clearly indicate purpose: `user_count` instead of `x`.

3. Write Documentation
Document your functions, classes, and modules with clear docstrings.

4. Keep Functions Small and Focused
Each function should do one thing and do it well. This makes testing and debugging easier.

5. Use List Comprehensions Wisely
They're powerful but can become unreadable. If it's complex, use a regular loop.

6. Handle Exceptions Properly
Catch specific exceptions and provide meaningful error messages.

7. Use Type Hints
Type hints improve code readability and help catch bugs early.

8. Write Tests
Comprehensive tests give you confidence to refactor and improve code.

9. Avoid Global Variables
They make code harder to understand and test. Pass data explicitly.

10. Refactor Regularly
Continuously improve your code as you learn better patterns and practices.

Clean code is not just about aesthetics—it's about creating maintainable, scalable applications that stand the test of time.''',
                'image': 'https://via.placeholder.com/800x500/06b6d4/ffffff?text=Clean+Code',
                'category': 'Best Practices',
                'tags': 'python, clean-code, best-practices, programming',
                'author': 'Admin',
                'date': datetime.utcnow() - timedelta(days=3)
            }
        ]
        
        for post_data in blog_posts:
            post = BlogPost(**post_data)
            db.session.add(post)
        
        # Commit all changes
        db.session.commit()
        print("\n✓ Sample data created successfully!")
        print(f"✓ Created {len(projects)} projects")
        print(f"✓ Created {len(blog_posts)} blog posts")
        print("\nYou can now run the application with 'python run.py'")


if __name__ == '__main__':
    print("="*60)
    print("Portfolio Database Initialization")
    print("="*60)
    init_sample_data()
