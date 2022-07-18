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

Creating Expense models and applying migrations
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