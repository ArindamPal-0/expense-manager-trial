# Expense Manager

### Full Stack django project

<br>

## Project creation steps:

### Project Setup

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
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Expense Manager</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor"
      crossorigin="anonymous"
    />
    <script
      defer
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2"
      crossorigin="anonymous"
    ></script>
  </head>
  <body>
    <h1>Expense Manager</h1>
  </body>
</html>
```

adding static compiled and minified bootstrap css and js.

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Expense Manager</title>

    <link href="/static/css/bootstrap.min.css" rel="stylesheet" />
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
        <div class="border border-white col-2">Column1</div>
        <div class="border border-white col">Column2</div>
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

### Creating the expense dashboard page

creating all the required routes with base template viz. index.html - dashboard and summary.html - summary.

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{% block title %}{% endblock title %} | Expense Manager</title>
    <!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script> -->

    <link href="/static/css/custom.css" rel="stylesheet" />
    <link href="/static/css/bootstrap.min.css" rel="stylesheet" />
    <script defer src="/static/js/bootstrap.min.js"></script>
  </head>
  <body>
    <div id="main" class="container-fluid d-flex flex-column">
      <!-- <div class="row">
        hello
      </div>
      <div class="row bg-dark text-light flex-grow-1">
        hello2
      </div> -->

      <!-- the navbar which shows only title -->
      <div class="row">
        <nav class="navbar navbar-expand-lg bg-dark navbar-dark">
          <div class="container-fluid">
            <a class="navbar-brand" href="/">Expense Manager</a>
          </div>
        </nav>
      </div>

      <!-- below navbar -->
      <div class="row flex-grow-1 bg-dark text-light">
        <!-- the side nav -->
        <div class="col-2 list-group p-0">
          <a
            href="/"
            class="custom-tab-width list-group-item list-group-item-action {% block expenseactive %}{% endblock expenseactive %}"
            >Expenses</a
          >
          <a
            href="/summary"
            class="custom-tab-width list-group-item list-group-item-action {% block summaryactive %}{% endblock summaryactive %}"
            >Summary</a
          >

          {% comment %}
          <a
            class="custom-tab-width row bg-dark text-light border border-light text-decoration-none d-flex flex-row align-items-center"
            href="/"
            ><div class="text-center">Expenses</div></a
          >
          <a
            class="custom-tab-width row bg-dark text-light border border-light text-decoration-none d-flex flex-row align-items-center"
            href="/summary"
            ><div class="text-center">Summary</div></a
          >
          {% endcomment %}

          <!-- <div class="custom-tab-width row bg-light text-dark border border-dark  d-flex flex-row align-items-center"><div class="text-center">Row</div></div> -->
        </div>

        <!-- content of the page -->
        <div
          class="col bg-light border-start border-top border-white p-0 overflow-auto"
        >
          <div
            class="container-fluid bg-dark h-100 mh-100 text-light d-flex flex-column justify-content-evenly"
          >
            {% block content %} {% endblock content %}
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
```

dashboard

```html
<!-- templates/index.html -->
{% extends "base.html" %} {% block title %}Expenses{% endblock title%} {% block
expenseactive %}active{% endblock expenseactive %} {% block content %}
<!-- Heading -->
<h1 class="text-center">Expenses</h1>

<!-- Search bar -->
<div class="row justify-content-center">
  <div class="col-6">
    <form class="d-flex" role="search">
      <input
        class="form-control me-2"
        type="search"
        placeholder="Search"
        aria-label="Search"
      />
      <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
  </div>
</div>

<!-- List of expenses server rendered -->
<div
  class="row justify-content-center"
  style="height: 70%; max-height: 70%; overflow-x: hidden; overflow-y: auto;"
>
  <div class="col-8 border border-2 rounded border-light p-1">
    <ul class="list-group">
      <!-- forloop template to render all the expenses in a list -->
      {% for expense in expenses %}
      <li class="list-group-item">{{expense.name}}</li>
      {% endfor %}
    </ul>
  </div>
</div>

<!-- Add Expense Form -->
<div class="row justify-content-center">
  <div class="col-10">
    <form action="/" method="POST">
      <div class="row">
        <div class="col-6">
          <input
            type="text"
            class="form-control"
            placeholder="Expense name"
            aria-label="Expense name"
          />
        </div>
        <div class="col-3">
          <input
            type="text"
            class="form-control"
            placeholder="Amount"
            aria-label="Amount"
          />
        </div>
        <div class="col-3">
          <button type="submit" class="form-control lh-1 fs-6">
            Add Expense
          </button>
        </div>
      </div>
    </form>
  </div>
</div>
{% endblock content %}
```

summary page

```html
<!-- templates/summary.html -->
{% extends "base.html" %}

{% block title %}Summary{% endblock title%} 
{% block summaryactive %}active{% endblock summaryactive %}
{% block content %}summary{% endblock content %}
```

adding the necessary views, fetching and passing all the expenses in context and passing to the template in index view.

```python
# webapp/views.py
from expenses.models import Expense

# the default view or expenses view
def index(request):
    # getting all the expenses
    expenses = Expense.objects.all()

    # passing the expenses to the template
    context = {
        'expenses': expenses
    }

    # rendering the template
    return render(request, 'index.html', context=context)
```
