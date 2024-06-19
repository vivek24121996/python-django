from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Jan Text",
    "february": "Feb Text",
    "march": "March Text",
    "april": "April Text",
    "may": "May Text",
    "june": "June Text",
    "july": "July Text",
    "august": "August Text",
    "september": "September Text",
    "october": "October Text",
    "november": "November Text",
    "december": "Decemeber Text"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalised_month = month.capitalize()
        month_path = reverse("monthly_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\" >{capitalised_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

# Create your views here.
# def january(request):
#     return HttpResponse("jan Challenge")


# def february(request):
#     return HttpResponse("feb Challenge")

def monthly_challenge_by_month(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Month not found")
    
    redirect_month = months[month-1]
    redirect_path = reverse("monthly_challenge", args=[redirect_month])
    # return HttpResponseRedirect("/challenges/" + redirect_month) 
    # to avoid hard core redirect URL
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        # return HttpResponse(text)
        response_data = f"<h1>{text}</h1>"
        return HttpResponse(response_data)
    except:
        # return HttpResponseNotFound("No month text found")
        return HttpResponseNotFound("<h1>No month text found</h1>")
