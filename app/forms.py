"""
Flask WTForms
"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, URLField, DateField
from wtforms.validators import DataRequired, Email, Length, Optional, URL


class ContactForm(FlaskForm):
    """Contact form with validation"""
    name = StringField('Name', validators=[
        DataRequired(message='Name is required'),
        Length(min=2, max=100, message='Name must be between 2 and 100 characters')
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Email is required'),
        Email(message='Invalid email address')
    ])
    subject = StringField('Subject', validators=[
        DataRequired(message='Subject is required'),
        Length(min=5, max=200, message='Subject must be between 5 and 200 characters')
    ])
    message = TextAreaField('Message', validators=[
        DataRequired(message='Message is required'),
        Length(min=10, max=2000, message='Message must be between 10 and 2000 characters')
    ])
    submit = SubmitField('Send Message')


class LoginForm(FlaskForm):
    """Admin login form"""
    username = StringField('Username', validators=[
        DataRequired(message='Username is required')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required')
    ])
    submit = SubmitField('Login')


class ProjectForm(FlaskForm):
    """Project creation/edit form"""
    title = StringField('Title', validators=[
        DataRequired(message='Title is required'),
        Length(min=3, max=200)
    ])
    slug = StringField('Slug', validators=[
        DataRequired(message='Slug is required'),
        Length(min=3, max=200)
    ])
    description = TextAreaField('Description', validators=[
        DataRequired(message='Description is required')
    ])
    image = URLField('Image URL', validators=[Optional(), URL()])
    technology_stack = StringField('Technology Stack (comma-separated)', validators=[
        DataRequired(message='Technology stack is required')
    ])
    github_url = URLField('GitHub URL', validators=[Optional(), URL()])
    live_demo_url = URLField('Live Demo URL', validators=[Optional(), URL()])
    category = StringField('Category', validators=[
        DataRequired(message='Category is required'),
        Length(max=100)
    ])
    features = TextAreaField('Features (one per line)', validators=[Optional()])
    submit = SubmitField('Save Project')


class BlogPostForm(FlaskForm):
    """Blog post creation/edit form"""
    title = StringField('Title', validators=[
        DataRequired(message='Title is required'),
        Length(min=3, max=200)
    ])
    slug = StringField('Slug', validators=[
        DataRequired(message='Slug is required'),
        Length(min=3, max=200)
    ])
    content = TextAreaField('Content', validators=[
        DataRequired(message='Content is required')
    ])
    image = URLField('Image URL', validators=[Optional(), URL()])
    category = StringField('Category', validators=[
        DataRequired(message='Category is required'),
        Length(max=100)
    ])
    tags = StringField('Tags (comma-separated)', validators=[Optional()])
    author = StringField('Author', validators=[
        DataRequired(message='Author is required'),
        Length(max=100)
    ])
    submit = SubmitField('Save Post')
