from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")    
    