from django.urls import path
from feghomeapp_eng import views

urlpatterns = [
    path('', views.home_eng, name='home_eng'),
    path('intro/intro_eng/', views.intro_eng, name='intro_eng'),
    path('intro/history_eng/', views.history_eng, name='history_eng'),
    path('intro/ogchart_eng/', views.ogchart_eng, name='ogchart_eng'),
    path('intro/sponsorship_eng/', views.sponsorship_eng, name='sponsorship_eng'),    
    path('intro/access_eng/', views.access_eng, name='access_eng'),        
    path('maintask/sea_eng/', views.sea_eng, name='sea_eng'),     
    path('maintask/air_eng/', views.air_eng, name='air_eng'),          
    path('corevalue/corevalue_eng/', views.corevalue_eng,name='corevalue_eng'),      
    path('corevalue/rational_price_eng/', views.rational_price_eng,name='rational_price_eng'),  
    path('travel_eng', views.travel_eng,name='travel_eng'),     
    path('inquiry_eng', views.inquiry_eng,name='inquiry_eng'),                                
]