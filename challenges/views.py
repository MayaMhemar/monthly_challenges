from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "fabruary" : "Walk for at least 20 minutes every day!",
    "march" : "Learn Django for at least 20 minutes every day!",
    "april" : "Walk for at least 20 minutes every day!",
    "may" :"Eat no meat for the entire month!",
    "june" : "Walk for at least 20 minutes every day!",
    "july" : "Learn Django for at least 20 minutes every day!",
    "august" :"Eat no meat for the entire month!",
    "september" : "Walk for at least 20 minutes every day!",
    "october" : "Learn Django for at least 20 minutes every day!",
    "november" :"Eat no meat for the entire month!",
    "december" : "Walk for at least 20 minutes every day!"
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args = [month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month  > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")    
    