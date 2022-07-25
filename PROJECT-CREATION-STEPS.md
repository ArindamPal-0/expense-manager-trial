# Expense Manager
### Full Stack django project

<br>

## Project creation steps:

Env Setup (Windows)
```Powershell
$ python -m venv .venv
$ .venv/Scripts/Activate.ps1
(.venv)$ pip install django
```

Basic Django Project Setup (Windows)
```Powershell
(.venv)$ django-admin startporject expenses .
(.venv)$ python manage.py migrate
(.venv)$ python manage.py runserver
```

Creating superuser to access admin panel of the project
```Powershell
(.venv)$ python manage.py createsuperuser
```

### Creating Expense models and applying migrations

```python
# expenses/models.py
from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.name + ' - ₹ ' + str(self.amount) + ' - ' + str(self.date)
```

```Powershell
(.venv)$ python manage.py makemigrations expenses
(.venv)$ python manage.py migrate
```

Adding the model to the admin panel
```python
# expenses/admin.py
from django.contrib import admin
from expenses.models import Expense

admin.site.register(Expense)
```
now restart the server to see the changes.


start django shell to add records for the created model or use admin panel
```Powershell
(.venv)$ python manage.py shell
```

```python
from expenses.models import Expense
from datetime import datetime

e = Expense(name="samosa", amount=10, date=datetime.now())
e.save()
```

### Creating the webapp

```Powershell
(.venv)$ python manage.py startapp webapp
```

now then create the view for the webapp
```python
# webapp/views.py
fron django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

here we are making use of templates, but we did not setup templates yet.
Setting up templates and static files.
Create `templates` and `static folder` in the root project directory.
Now setup `templates` and `static folder` in the settings.py directory, also add the `webapp` in the `INSTALLED_APP` list.

```python
# expenses/settings.py

INSTALLED_APPS = [
    'expenses',
    'webapp',
    ...
]

TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    }
]

STATICFILES_DIRS = [BASE_DIR / 'static']
```

now adding the url for the views.
setting url for the webapp in the base app.
```python
# expenses/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
]
```

url for the webapp
```python
# webapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home")
]
```

creating the index.html basic template with bootstrap setup
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Expense Manager</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
  </head>
  <body>
    <h1>Expense Manager</h1>
  </body>
</html>
```


adding static compiled and minified bootstrap css and js.

```html
<!-- index.html -->
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Expense Manager</title>

    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <script defer src="/static/js/bootstrap.min.js"></script>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg bg-dark navbar-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">Expense Manager</a>
      </div>
    </nav>
    <div class="bg-dark text-white container-flex">
      <div class="row bg-success">
        <div class="border border-white col-2">
          Column1
        </div>
        <div class="border border-white col">
          Column2
        </div>
      </div>
    </div>
  </body>
</html>
```

### using pipenv dev environment

Install `pipenv` if not already installed, make sure to open Powershell as administrator.
```Powershell(admin)
$ pip install pipenv
```

Activate virtual environment and install dependencies.
```Powershell
$ mkdir .venv
$ pipenv shell
$ pipenv install django
$ python manage.py runserver # running server is same as before
```

To exit the virtual environment, use the `exit` command.

