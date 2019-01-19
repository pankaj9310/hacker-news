Basic Commands
--------------
Setting project on local
^^^^^^^^^^^^^^^^^^^^^
* set database name and password in settings/base.py @line 82,83 ::

	$ sudo apt-get install python python-dev python-pip virtualenv
	$ virtualenv venv_hackernews
	$ source venv_nimoy/bin/activate
	$ pip install -r requirements.txt
	$ python manage.py makemigrations
	$ python manage.py migrate
	$ python manage.py runserver
