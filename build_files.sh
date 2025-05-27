# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p staticfiles_build/static

# Collect static files
python manage.py collectstatic --noinput 