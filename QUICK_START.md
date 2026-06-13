# 🚀 Quick Start Guide

Get your Flask Portfolio website running in **5 minutes**!

---

## ⚡ Installation (4 Commands)

### Windows:
```bash
cd portfolio
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python init_data.py
python run.py
```

### macOS/Linux:
```bash
cd portfolio
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python init_data.py
python run.py
```

---

## 🌐 Access Your Website

Once running, open your browser:

### Main Website
```
http://127.0.0.1:5000
```

### Admin Panel
```
http://127.0.0.1:5000/admin/login
```

**Default Login:**
- Username: `admin`
- Password: `admin123`

---

## 📄 Pages Available

| Page | URL | Description |
|------|-----|-------------|
| **Home** | `/` | Hero section, stats, featured projects |
| **About** | `/about` | Biography, skills, timeline |
| **Projects** | `/projects` | All projects with filters |
| **Services** | `/services` | Service offerings |
| **Blog** | `/blog` | Blog posts listing |
| **Contact** | `/contact` | Contact form |
| **Admin** | `/admin/login` | Admin panel login |

---

## 🎨 Quick Customization

### 1. Change Your Name
**File:** `templates/index.html`  
**Line:** Find `John Doe` and replace with your name

### 2. Update Profile Image
**File:** `templates/index.html`  
**Line:** Replace the image URL or add your image to `static/images/`

### 3. Modify Colors
**File:** `static/css/main.css`  
**Lines:** Edit CSS variables at the top:
```css
:root {
    --primary-color: #6366f1;  /* Change this */
    --secondary-color: #8b5cf6; /* And this */
}
```

### 4. Add Your Social Links
**File:** `templates/base.html` (footer section)  
**Update:** Replace `https://github.com` with your actual links

---

## 🎯 Admin Panel Guide

### Add a Project
1. Login to admin panel
2. Click "Projects" in sidebar
3. Click "Create New Project"
4. Fill in:
   - Title: Project name
   - Slug: URL-friendly name (e.g., `my-project`)
   - Description: What the project does
   - Technology Stack: `Python, Flask, etc.` (comma-separated)
   - Category: `Web Application`, `API`, etc.
   - Features: One per line
   - URLs: GitHub and/or Live Demo
5. Click "Save Project"

### Write a Blog Post
1. Login to admin panel
2. Click "Blog Posts" in sidebar
3. Click "Create New Post"
4. Fill in:
   - Title: Post title
   - Slug: URL-friendly (e.g., `my-first-post`)
   - Content: Your article content
   - Category: `Tutorial`, `News`, etc.
   - Tags: `python, flask` (comma-separated)
   - Author: Your name
5. Click "Save Post"

### View Messages
1. Login to admin panel
2. Click "Messages" in sidebar
3. Click any message to view details
4. Messages automatically marked as read

---

## 🛠 Sample Data

The `init_data.py` script creates:
- ✅ 6 Sample Projects
- ✅ 5 Sample Blog Posts
- ✅ Admin user (admin/admin123)

**To reset data:**
```bash
# Delete the database
rm instance/database.db

# Run the app to recreate
python run.py

# Add sample data again
python init_data.py
```

---

## 🎨 Features You Can Use

### Dark Mode
- Click the moon/sun icon in the navbar
- Preference is saved in browser

### Search & Filter
- **Projects page**: Search by keyword or filter by category
- **Blog page**: Search posts or filter by category

### Responsive Design
- Automatically works on:
  - 📱 Mobile phones
  - 📱 Tablets
  - 💻 Laptops
  - 🖥️ Desktops

---

## 🔒 Security Tips

### Before Production:
1. **Change admin password**
   ```python
   # In Python shell or add to init_data.py
   admin = AdminUser.query.filter_by(username='admin').first()
   admin.set_password('your-secure-password')
   db.session.commit()
   ```

2. **Change secret key**  
   **File:** `app/__init__.py`
   ```python
   app.config['SECRET_KEY'] = 'your-random-secret-key-here'
   ```

3. **Use environment variables**
   ```python
   import os
   app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
   ```

---

## 📚 File Locations

### To Edit Content:
- **Home page text**: `templates/index.html`
- **About page bio**: `templates/about.html`
- **Services**: `templates/services.html`
- **Footer links**: `templates/base.html`

### To Change Styles:
- **Colors & fonts**: `static/css/main.css`
- **Animations**: Already set up in CSS
- **Dark theme colors**: In `:root` and `[data-bs-theme="dark"]`

### To Modify Functionality:
- **Routes**: `app/routes.py`
- **Database models**: `app/models.py`
- **Forms**: `app/forms.py`
- **JavaScript**: `static/js/main.js`

---

## 🚨 Troubleshooting

### Port Already in Use?
**Fix:** Change port in `run.py`:
```python
app.run(debug=True, host='127.0.0.1', port=5001)  # Change 5000 to 5001
```

### Can't Activate Virtual Environment?
**Windows PowerShell:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Database Not Found?
**Fix:** Just run the app once, it auto-creates:
```bash
python run.py
```

### Import Errors?
**Fix:** Make sure venv is activated:
```bash
# Check if (venv) appears in prompt
# If not, activate again:
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

---

## 📦 What's Included

| Component | Status | Location |
|-----------|--------|----------|
| Flask App | ✅ Complete | `app/` |
| Templates | ✅ 18 files | `templates/` |
| Styling | ✅ Custom CSS | `static/css/` |
| JavaScript | ✅ Interactive | `static/js/` |
| Database | ✅ Auto-created | `instance/` |
| Admin Panel | ✅ Full-featured | `/admin/*` |
| Documentation | ✅ Comprehensive | `*.md` files |

---

## 🎓 Next Steps

1. ✅ **Install & Run** (you're here!)
2. 📝 **Customize** your information
3. 🎨 **Add** your own projects and blog posts
4. 🖼️ **Replace** placeholder images
5. 🎨 **Adjust** colors to match your brand
6. 🚀 **Deploy** to hosting platform

---

## 💡 Tips

### Add Your Own Images
1. Save images to `static/images/`
2. Use in templates: `{{ url_for('static', filename='images/yourimage.jpg') }}`

### Change Typing Effect Text
**File:** `templates/index.html`  
**Find:** The `texts` array in JavaScript and edit the strings

### Modify Statistics Numbers
**File:** `templates/index.html`  
**Find:** `data-target="50"` and change numbers

---

## 📞 Need Help?

Check these files:
- 📖 **README.md** - Full documentation
- ✅ **VERIFICATION.md** - Complete feature list
- 📊 **PROJECT_SUMMARY.md** - Technical details

---

**Ready to build your portfolio? Let's go! 🚀**

```bash
python run.py
```

Then open: http://127.0.0.1:5000
