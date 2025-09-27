import random
import os
from django.shortcuts import render
from .forms import BusinessForm
import joblib

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')



def loading(request):
    return render(request, 'loadingPage.html')







def predict_success(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            # Load the trained model
            model_path = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')
            model = joblib.load(model_path)

            # Get form data
            revenue = form.cleaned_data['revenue']
            cost_of_goods_sold = form.cleaned_data['cost_of_goods_sold']
            operating_expenses = form.cleaned_data['operating_expenses']

            # Make prediction
            predicted_success_rate = model.predict([[revenue, cost_of_goods_sold, operating_expenses]])[0]

            # Generate randomized suggestions based on predicted success rate
            suggestions_high = [
                "Your business is on track for great success! Keep up the good work.",
                "Consider expanding your operations to capitalize on your current momentum.",
                "Invest in innovation to stay ahead of the competition."
            ]
            suggestions_medium = [
                "Your business is doing well, but there's room for improvement.",
                "Focus on optimizing your expenses to increase profitability.",
                "Explore new marketing strategies to attract more customers."
            ]
            suggestions_low = [
                "Your business may be facing challenges. Evaluate your strategies and make necessary adjustments.",
                "Seek expert advice to identify areas for improvement and develop a plan for recovery.",
                "Consider diversifying your revenue streams to mitigate risks."
            ]
            

            # Select suggestions based on predicted success rate
            if predicted_success_rate > 70:
                suggestions = random.sample(suggestions_high, k=2)
                success_indicator = "High"
            elif predicted_success_rate > 50:
                suggestions = random.sample(suggestions_medium, k=2)
                success_indicator = "Medium"
            else:
                suggestions = random.sample(suggestions_low, k=2)
                success_indicator = "Low"

            # Display prediction result, suggestions, and indicators
            return render(request, 'resultPage.html', {'predicted_success_rate': predicted_success_rate, 'suggestions': suggestions, 'success_indicator': success_indicator})
    else:
        form = BusinessForm()
    return render(request, 'inputPage.html', {'form': form})
