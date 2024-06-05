from django.db import models
import datetime

class Currency(models.Model):
    code = models.CharField(max_length=20)
    rate = models.DecimalField(max_digits=15, decimal_places=8, null=True)
    date = models.DateField(default=datetime.date.today)
    class Meta:
        app_label = 'currencyAPI'