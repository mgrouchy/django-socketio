Django Socket.io
=================

#### A socketio implementation for django

*As an advisement I would not use this for anything, this was a proof of concept
it doesn't work very well and is left here only for posterity.*


#### Using it

Add django_socketio to your installed apps

```python
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
     'django.contrib.admindocs',
    'django_socketio',
)
```


Now you can run the socketio server

```shell
./manage.py runserver_socketio 127.0.0.1:8000
```

or you can use the socketio gunicorn worker.

```shell
django_gunicorn --worker-class django_socketio.gunicorn.workers.GeventSocketIOWorker
#or
./manage.py run_gunicorn --worker-class django_socket.io.gunicorn.workers.GeventSocketIOWorker
```


Ensure you have a view with the endpoint

yourwebsite.com/socket.io and you are good to go from django side of things



#### settings

there are no settings currently, but there will be soon.


