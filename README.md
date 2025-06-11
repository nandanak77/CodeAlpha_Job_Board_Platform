CodeAlpha_Job_Board_Platform


This is a Django-based Job Board Platform designed to connect employers with job seekers. It allows employers to post job listings and candidates to view and apply for them through a simple and clean user interface built with HTML, CSS, and JavaScript.

## Features

- User Registration and Login
- Employer Dashboard for posting jobs
- Job Seeker Dashboard to apply for jobs
- Resume uploads with file handling
- Django Admin Panel for managing data
- Responsive frontend with templates and static files

##  Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Database: SQLite (default)

## 🚀 Getting Started


1. **Set up Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

2. **Install Requirements:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations & Server:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to use the app.

