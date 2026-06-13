# 🚀 Flask Portfolio Website

A modern, responsive personal portfolio website built with **Python Flask**. Features a complete admin panel, blog system, project showcase, and contact management.

![Portfolio Screenshot](https://via.placeholder.com/1200x600/667eea/ffffff?text=Portfolio+Website)

## ✨ Features

### 🎨 Frontend
- **Modern & Responsive Design** - Works perfectly on all devices
- **Dark/Light Mode** - Toggle between themes with local storage persistence
- **Smooth Animations** - AOS library for scroll animations
- **Glassmorphism Effects** - Modern UI design patterns
- **Bootstrap 5** - Latest Bootstrap framework
- **Bootstrap Icons** - Beautiful icon set

### 🏠 Public Pages
- **Home** - Hero section with typing effect and animated statistics
- **About** - Biography, skills progress bars, experience timeline
- **Projects** - Showcase with search, category filter, and pagination
- **Services** - Display your service offerings
- **Blog** - Full-featured blog with categories and tags
- **Contact** - Validated contact form with database storage

### 🔐 Admin Panel
- **Secure Authentication** - Login system with session management
- **Dashboard** - Statistics and quick overview
- **Project Management** - Full CRUD operations
- **Blog Management** - Create, edit, and delete posts
- **Message Management** - View and manage contact form submissions

### 🛠 Technical Features
- **Flask Blueprints** - Modular application structure
- **SQLAlchemy ORM** - Database management
- **Flask-WTF** - Form handling with CSRF protection
- **Flask-Migrate** - Database migrations
- **Jinja2 Templates** - Powerful templating engine
- **SQLite Database** - Lightweight and portable
- **RESTful Design** - Clean URL structure
- **SEO Friendly** - Optimized for search engines

## 📋 Requirements

- Python 3.11 or higher
- pip (Python package manager)

## 🚀 Installation

### 1. Clone or Download

```bash
# If you have the project folder, navigate to it
cd portfolio
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application (First Time)

```bash
python run.py
```

**Important**: On first run, the application will:
- ✅ Create the database
- ✅ Create database tables
- ✅ Create default admin user (admin/admin123)

The application will notify you if the database is empty.

### 5. Add Sample Data (Optional)

To populate the database with sample projects and blog posts:

```bash
python init_data.py
```

This will add:
- 6 sample projects
- 5 sample blog posts

### 6. Access the Application

The application will be available at:
- **Website**: http://127.0.0.1:5000
- **Admin Panel**: http://127.0.0.1:5000/admin/login

## 🎯 Default Credentials

```
Username: admin
Password: admin123
```

⚠️ **Important**: Change the default credentials in production!

## 📁 Project Structure

```
portfolio/
│
├── app/
│   ├── __init__.py          # Application factory
│   ├── models.py            # Database models
│   ├── forms.py             # WTForms definitions
│   └── routes.py            # Application routes
│
├── templates/
│   ├── base.html            # Base template
│   ├── index.html           # Home page
│   ├── about.html           # About page
│   ├── projects.html        # Projects listing
│   ├── project_detail.html  # Project detail
│   ├── services.html        # Services page
│   ├── blog.html            # Blog listing
│   ├── blog_detail.html     # Blog post detail
│   ├── contact.html         # Contact page
│   └── admin/               # Admin templates
│       ├── base.html        # Admin base
│       ├── login.html       # Admin login
│       ├── dashboard.html   # Dashboard
│       ├── projects.html    # Manage projects
│       ├── blog.html        # Manage blog
│       └── messages.html    # View messages
│
├── static/
│   ├── css/
│   │   └── main.css         # Custom styles
│   ├── js/
│   │   └── main.js          # Custom JavaScript
│   └── images/              # Image assets
│
├── instance/
│   └── database.db          # SQLite database (auto-created)
│
├── run.py                   # Application entry point
├── init_data.py             # Sample data script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🎨 Customization

### Update Personal Information

1. **Templates** - Edit text in template files
2. **Colors** - Modify CSS variables in `static/css/main.css`
3. **Images** - Replace placeholder images with your own
4. **Social Links** - Update URLs in templates

### Add New Projects

1. Login to admin panel
2. Navigate to "Projects"
3. Click "Create New Project"
4. Fill in the form and save

### Write Blog Posts

1. Login to admin panel
2. Navigate to "Blog Posts"
3. Click "Create New Post"
4. Write your content and publish

## 🔒 Security

- CSRF protection enabled on all forms
- Password hashing with Werkzeug
- Input validation with WTForms
- SQL injection protection via SQLAlchemy ORM
- XSS protection with Jinja2 auto-escaping

## 🌐 Deployment

### Heroku

```bash
# Install Heroku CLI and login
heroku login

# Create new app
heroku create your-app-name

# Add PostgreSQL database
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key

# Deploy
git push heroku main
```

### DigitalOcean

1. Create a Droplet
2. Install Python and dependencies
3. Set up Nginx as reverse proxy
4. Use Gunicorn as WSGI server
5. Configure SSL with Let's Encrypt

### PythonAnywhere

1. Upload project files
2. Create virtual environment
3. Configure WSGI file
4. Set up static files
5. Start web app

## 📚 Technologies Used

### Backend
- **Flask 3.0.0** - Web framework
- **SQLAlchemy 3.1.1** - ORM
- **Flask-WTF 1.2.1** - Forms
- **Flask-Migrate 4.0.5** - Database migrations
- **Werkzeug 3.0.1** - WSGI utilities

### Frontend
- **Bootstrap 5.3.2** - CSS framework
- **Bootstrap Icons** - Icon set
- **AOS 2.3.1** - Scroll animations
- **Vanilla JavaScript** - Interactivity

### Database
- **SQLite** - Development database
- (Easy to migrate to PostgreSQL/MySQL)

## 🐛 Troubleshooting

### Virtual Environment Not Activating

**Windows**:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Import Errors

Make sure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Database Not Found

Run the application once to auto-create the database:
```bash
python run.py
```

### Port Already in Use

Change the port in `run.py`:
```python
app.run(debug=True, host='127.0.0.1', port=5001)
```

## 📸 Screenshots

### Home Page
![Home](https://via.placeholder.com/800x500/667eea/ffffff?text=Home+Page)

### Projects
![Projects](https://via.placeholder.com/800x500/8b5cf6/ffffff?text=Projects)

### Blog
![Blog](https://via.placeholder.com/800x500/10b981/ffffff?text=Blog)

### Admin Dashboard
![Admin](https://via.placeholder.com/800x500/f59e0b/ffffff?text=Admin+Dashboard)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Your Name**

- Website: [yourwebsite.com](https://yourwebsite.com)
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourname)

## ⭐ Show your support

Give a ⭐️ if this project helped you!

## 📞 Contact

For questions or support, please use the contact form on the website or reach out via:

- Email: contact@yourwebsite.com
- Telegram: [@yourusername](https://t.me/yourusername)

---

**Built with ❤️ using Flask and Bootstrap**
