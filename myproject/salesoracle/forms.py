from django import forms

class BusinessForm(forms.Form):
    revenue = forms.FloatField(label='Revenue')
    cost_of_goods_sold = forms.FloatField(label='Cost of Goods Sold')
    operating_expenses = forms.FloatField(label='Operating Expenses')
