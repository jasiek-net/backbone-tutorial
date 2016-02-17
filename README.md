# backbone-tutorial

I found simple BackboneJS tutorial at yt (https://youtu.be/FZSjvWtUxYk) but without backend, so I wrote simple API in Django, independent from client-side (with CORS - Cross-Origin Resource Sharing, it's just a practies, not safe).

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
