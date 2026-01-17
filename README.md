# Django Blog Project

A simple blog application built with Django 6.0.1 that allows users to view blog posts.

## Features

- View list of all blog posts
- View individual blog post details
- Admin interface for managing posts
- Responsive design with custom CSS

## Project Structure

```
myproject/
├── myproject/          # Main project configuration
├── posts/              # Blog posts app
├── templates/          # Global templates
├── static/             # Static files (CSS, JS)
├── db.sqlite3          # SQLite database
└── manage.py           # Django management script
```

## Installation

1. Clone or download the project
2. Create a virtual environment:
   ```
   python -m venv .venv
   ```
3. Activate the virtual environment:
   ```
   .venv\Scripts\activate
   ```
4. Install Django:
   ```
   pip install django==6.0.1
   ```

## Usage

1. Run migrations:
   ```
   python manage.py migrate
   ```
2. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```
3. Start the development server:
   ```
   python manage.py runserver
   ```
4. Visit `http://127.0.0.1:8000/` to view the site

## URLs

- `/` - Homepage
- `/about/` - About page
- `/posts/` - List of all posts
- `/posts/<slug>/` - Individual post detail
- `/admin/` - Admin interface

## Models

### Post
- `title` - CharField (max 75 characters)
- `body` - TextField
- `slug` - SlugField (for URLs)
- `date` - DateTimeField (auto-generated)

## Requirements

- Python 3.14.2
- Django 6.0.1
