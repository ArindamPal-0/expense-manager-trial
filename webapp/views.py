from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from expenses.models import Expense

from datetime import date

# Create your views here.
# the default view or expenses view
def index(request: HttpRequest) -> HttpResponse:
    context: dict[str, any] = {}
    alerts: list[dict[str, str]] = []

    if request.session.has_key('alert'):
        alert = request.session.get('alert')
        request.session.pop('alert', None)
        print(alert)
        alerts.append(alert)
    else:
        print('no alert')

    # getting all the expenses
    expenses: list[Expense] = Expense.objects.all()

    # passing the expenses to the template
    context.update({
        'alerts': alerts,
        'expenses': expenses
    })

    # rendering the template
    return render(request, 'index.html', context=context)

# handling post requests from index view

# add expense view

def add_expense(request: HttpRequest) -> HttpResponse:
    alert: dict[str, str] | None = None

    # form submitted to add expense
    if request.method == 'POST':
        print('form submitted')

        # for getting all sorts of error in form data
        try:
            name: str | None = request.POST.get('expense_name')
            amountStr: str | None = request.POST.get('expense_amount')

            if name == None or amountStr == None:
                raise ValueError("name and amount should be provided.")

            if name == '' or amountStr == '':
                raise ValueError("name and amount should not be empty string.")

            # TODO: validate name and amount to avoid security failures

            # to get custom error message for invalid amount
            amount: float = 0.0
            try:
                amount = float(amountStr)
            except ValueError:
                raise ValueError("amount should be a number.")



            print(name, amount)

            # create the expense item and save it
            
            expense: Expense = Expense(name=name, amount=amount, date=date.today())
            expense.save()
            alert = {
                'style': 'success',
                'type': 'Success', 
                'message': 'Expense added successfully'
            }
        except ValueError as e:
            # do some kind of error handling
            # print('ValueError: cannot parse amount value to float')
            print(f'ValueError: {e}')
            alert = {
                'style': 'danger',
                'type': 'Error', 
                'message': str(e),
            }
    
    if alert is not None:
        request.session['alert'] = alert

    return redirect('home')

# update expense view

def update_expense(request: HttpRequest) -> HttpResponse:
    return redirect('home')

# delete expense view

def delete_expense(request: HttpRequest) -> HttpResponse:
    alert: dict[str, str] | None = None

    # form submitted to delete expense
    if request.method == 'POST':
        print('delete form submitted')

        try:
            # get id from the POST request
            idStr: str | None = request.POST.get('id')
            print(type(idStr) == str)
            print(idStr)

            # convert id from str to int
            id: int = int(idStr)

            # TODO: Check if id is valid

            # query expense object based on id
            expense: Expense = Expense.objects.get(id=id)

            print(expense)

            # deleting the expense record
            print(expense.delete())

            alert = {
                'style': 'success',
                'type': 'Success',
                'message': f"Successfully deleted expense with id {id}"
            }

        except Exception as e:
            print(f'error deleting record: {e}')
            alert = {
                "style": "danger",
                "type": "Error",
                "message": "Couldn't delete the expense"
            }

        # adding alert to session if alert exists
        if alert is not None:
            request.session['alert'] = alert

    return redirect('home')

# the summary view
def summary(request: HttpRequest) -> HttpResponse:
    return render(request, 'summary.html')
