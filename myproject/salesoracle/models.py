# predictor/models.py

from django.db import models

class Prediction(models.Model):
    month = models.CharField(max_length=20)
    sales_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    cost_of_goods_sold = models.DecimalField(max_digits=10, decimal_places=2)
    operating_expenses = models.DecimalField(max_digits=10, decimal_places=2)
    gross_profit = models.DecimalField(max_digits=10, decimal_places=2)
    net_profit = models.DecimalField(max_digits=10, decimal_places=2)
    success_rate = models.DecimalField(max_digits=5, decimal_places=2)
