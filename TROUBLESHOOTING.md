# Troubleshooting Guide

Common issues and their solutions for the Flask Portfolio Website.

---

## Error: "TemplateNotFound: index.html"

**Symptom:**
```
jinja2.exceptions.TemplateNotFound: index.html
```

**Cause:**
Flask couldn't find the templates folder.

**Solution:**
✅ **Already Fixed** in commit `50a3a02`

The `app/__init__.py` now explicitly specifies template and static folder paths. Simply pull the latest changes:

```bash
git pull origin main
```

---

## Error: "no such table: projects"

**Symptom:**
```
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: projects
```

**Cause:**
Running `init_data.py` before the database tables are created.

**Solution:**
✅ **Already Fixed** in commit `121032c`

Run the application first to create tables:

```bash
python run.py
```

Then optionally add sample data:

```bash
# Stop the app (Ctrl+C)
python init_data.py
# Restart the app
python run.py
```

---

## Error: "ModuleNotFoundError: No module named 'flask'"

**Symptom:**
```
ModuleNotFoundError: No module named 'flask'
```

**Cause:**
Dependencies not installed or virtual environment not activated.

**Solution:**

1. Activate virtual environment:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Error: Port 5000 already in use

**Symptom:**
```
OSError: [Errno 48] Address already in use
```

**Cause:**
Another application is using port 5000.

**Solution:**

**Option 1:** Kill the process using port 5000
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9
```

**Option 2:** Change the port in `run.py`
```python
app.run(debug=True, host='127.0.0.1', port=5001)  # Use port 5001 instead
```

---

## Error: "Permission denied" when creating virtual environment

**Symptom (Windows):**
```
cannot be loaded because running scripts is disabled on this system
```

**Solution:**
Run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Database is empty / No projects or blog posts

**Symptom:**
Website runs but shows empty pages.

**Cause:**
Sample data not added.

**Solution:**

1. Stop the application (Ctrl+C)
2. Run the sample data script:
```bash
python init_data.py
```
3. Restart the application:
```bash
python run.py
```

This will add 6 sample projects and 5 sample blog posts.

---

## Can't login to admin panel

**Default Credentials:**
- **Username:** `admin`
- **Password:** `admin123`

**If login still fails:**

1. Check if admin user exists in database
2. Recreate admin user by deleting `instance/database.db` and running `python run.py` again

---

## Static files (CSS/JS) not loading

**Symptom:**
Website loads but has no styling or JavaScript doesn't work.

**Cause:**
Flask can't find the static folder.

**Solution:**
✅ **Already Fixed** in commit `50a3a02`

The static folder path is now explicitly set. Pull the latest changes:

```bash
git pull origin main
```

**Verify static files exist:**
```bash
ls static/css/main.css
ls static/js/main.js
```

---

## Virtual environment issues

**Symptom:**
Can't activate or create virtual environment.

**Solutions:**

**Windows:**
```bash
# Ensure Python is in PATH
python --version

# Create venv
python -m venv venv

# Activate
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Ensure Python 3 is installed
python3 --version

# Create venv
python3 -m venv venv

# Activate
source venv/bin/activate
```

---

## Database locked error

**Symptom:**
```
sqlite3.OperationalError: database is locked
```

**Cause:**
Multiple processes accessing the database or incomplete transaction.

**Solution:**

1. Stop all running instances of the application
2. Delete the database and recreate:
```bash
# Stop the app
# Delete database
rm instance/database.db  # macOS/Linux
del instance\database.db  # Windows

# Restart app (creates fresh database)
python run.py

# Add sample data
python init_data.py
```

---

## Import errors

**Symptom:**
```
ImportError: cannot import name 'X' from 'app'
```

**Cause:**
Outdated dependencies or missing packages.

**Solution:**

1. Update pip:
```bash
python -m pip install --upgrade pip
```

2. Reinstall all dependencies:
```bash
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

---

## Need Help?

If you encounter an issue not listed here:

1. **Check the logs** - Look at the full error message
2. **Verify installation** - Make sure all steps were followed
3. **Check GitHub Issues** - https://github.com/Abdulaziz168/flask-portfolio-website/issues
4. **Create a new issue** - Describe the problem with error messages

---

## Quick Health Check

Run these commands to verify everything is set up correctly:

```bash
# 1. Check Python version (should be 3.11+)
python --version

# 2. Check if virtual environment is active
# Should show (venv) in your prompt

# 3. Check if dependencies are installed
pip list | grep Flask

# 4. Check if templates folder exists
ls templates/index.html

# 5. Check if static files exist
ls static/css/main.css
ls static/js/main.js

# 6. Try running the app
python run.py
```

All checks should pass ✅

---

**Last Updated:** June 13, 2024  
**Version:** 1.0.1
