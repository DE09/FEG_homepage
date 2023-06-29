from django.shortcuts import render , redirect
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.
def home_eng(request):
    return render(request, 'home_eng.html')




# 회사소개 페이지

def intro_eng(request):
    return render(request, 'intro/intro_eng.html')

def history_eng(request):
    return render(request, 'intro/history_eng.html')

def ogchart_eng(request):
    return render(request, 'intro/ogchart_eng.html')

def sponsorship_eng(request):
    return render(request, 'intro/sponsorship_eng.html')

def access_eng(request):
    return render(request, 'intro/access_eng.html')


# 주요업무 페이지

def sea_eng(request):
    return render(request, 'maintask/sea_eng.html')

def air_eng(request):
    return render(request, 'maintask/air_eng.html')


# 코어밸류

def corevalue_eng(request):
    
    return render(request, 'corevalue/corevalue_eng.html')

def rational_price_eng(request):
    return render(request, 'corevalue/rational_price_eng.html')


# 여행
def travel_eng(request):
    return render(request, 'travel_eng.html')

# 게시판
def inquiry_eng(request):
    return render(request, 'inquiry_eng.html')

