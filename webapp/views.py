from django.shortcuts import render
from expenses.models import Expense

# Create your views here.
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

# the summary view
def summary(request):
    return render(request, 'summary.html')
