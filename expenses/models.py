from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.name + ' - ₹ ' + str(self.amount) + ' - ' + str(self.date)