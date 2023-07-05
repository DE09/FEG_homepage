from django.urls import path
from feghomeapp_cn import views

urlpatterns = [
    path('home_cn', views.home_cn, name='home_cn'),
    path('intro/intro_cn/', views.intro_cn, name='intro_cn'),
    path('intro/history_cn/', views.history_cn, name='history_cn'),

    path('intro/ogchart_cn/', views.ogchart_cn, name='ogchart_cn'), 
    path('intro/sponsorship_cn/', views.sponsorship_cn, name='sponsorship_cn'),     
    path('intro/access_cn/', views.access_cn, name='access_cn'),            

    path('maintask/sea_cn', views.sea_cn, name='sea_cn'),
    path('maintask/air_cn', views.air_cn, name='air_cn'),   

    
    path('fegsquare/inquiry_cn', views.inquiry_cn, name='inquiry_cn'),
    path('fegsquare/service_cn', views.service_cn, name='service_cn'),
    path('fegsquare/price_cn', views.price_cn, name='price_cn'),

        
    path('simfullo_cn/', views.simfullo_cn, name='simfullo_cn'),
    path('travel_cn/', views.travel_cn, name='travel_cn'),
]