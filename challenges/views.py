from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "fabruary" : "Walk for at least 20 minutes every day!",
    "march" : "Learn Django for at least 20 minutes every day!",
    "april" :"Eat no meat for the entire month!"
}
# Create your views here.

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "fabruary":
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text ="Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)