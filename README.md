# Django Project

This is a Django web application with a modern setup including Bootstrap 5 and other best practices.

## Setup Instructions

1. Create and activate a virtual environment:
   ```bash
   python -m venv env
   .\env\Scripts\activate  # Windows
   source env/bin/activate  # Linux/Mac
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with the following content:
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

- `templates/`: Contains HTML templates
- `static/`: Static files (CSS, JavaScript, images)
- `media/`: User-uploaded files
- `myproject/`: Main project configuration

## Features

- Bootstrap 5 integration
- Crispy Forms with Bootstrap 5 template pack
- Environment variables configuration
- Static and media files setup
- Base template with responsive navigation

## Development

To create a new app:
```bash
python manage.py startapp your_app_name
```

Remember to add your new app to `INSTALLED_APPS` in `settings.py`. 