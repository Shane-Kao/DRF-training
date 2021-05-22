# Install
```batch
pip install -r requirements.txt
```
# Show available subcommands
```batch
django-admin
```
# Create project
```batch
django-admin startproject django_api
```
# Run server
```batch
python manage.py runserver
```

# Start app
```batch
python manage.py startapp test_app
```

# Model
1. add `test_app.apps.TestAppConfig` to `INSTALLED_APPS` in `setting.py`
2. `python manage.py makemigrations test_app`
3. `python manage.py migrate test_app`

# Create superuser
1. `python manage.py migrate`
2. `python manage.py createsuperuser`