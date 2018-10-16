



export APP_SETTINGS="config.TestingConfig"
gunicorn --bind 0.0.0.0:8000 wsgi
