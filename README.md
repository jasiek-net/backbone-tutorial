# backbone-tutorial

I found simple backbone tutorial at yt (https://youtu.be/FZSjvWtUxYk) but without backend, so I wrote simple crud backend in Django (but without any backbone-django framework, so it's not safe - switch off csrf, switch on cors).

```
# Backend configuration
cd backend/userManager
sudo apt-get update
sudo apt-get install virtualenv python-pip
virtualenv venv
. ./venv/bin/activate
pip install django
pip install django-cors-headers
./manage.py makemigrations app
./manage.py migrate
./manage.py runserver

# in browser go to:
/path/to/file/index.html
```
