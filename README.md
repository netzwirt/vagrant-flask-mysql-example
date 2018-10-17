# Simple flask project

This is my personal skeleton for flask projects.


Start:

	cd /home/flask/base/ 
	. venv/bin/activate
	export APP_SETTINGS="config.DevelopmentConfig"
	gunicorn --bind 0.0.0.0:8000 app:app
	
Check it at 

	http://12.20.54.21:8000/