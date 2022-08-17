from django.shortcuts import render
from expenses.models import Expense

from datetime import date

# Create your views here.
# the default view or expenses view
def index(request):
    context: dict[str, any] = {}
    alerts: list[dict[str, str]] = []

    # if the any of the form is submitted
    if request.method == 'POST':
        print('form submitted')

        try:
            name: str = request.POST.get('expense_name')
            amountStr: str = request.POST.get('expense_amount')
            amount: float = float(amountStr)
            
            print(name, amount)

            # create the expense item and save it
            
            expense: Expense = Expense(name=name, amount=amount, date=date.today())
            expense.save()
            alerts.append(
                {
                    'style': 'success',
                    'type': 'Success', 
                    'message': 'Expense added successfully'
                }
            )
        except ValueError:
            # do some kind of error handling
            print('ValueError: cannot parse amount value to float')
            alerts.append(
                {
                    'style': 'danger',
                    'type': 'Error', 
                    'message': 'Enter a valid amount'
                }
            )


    # getting all the expenses
    expenses: list[Expense] = Expense.objects.all()

    # passing the expenses to the template
    context.update({
        'alerts': alerts,
        'expenses': expenses
    })

    # rendering the template
    return render(request, 'index.html', context=context)

# the summary view
def summary(request):
    return render(request, 'summary.html')
