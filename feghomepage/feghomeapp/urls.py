from django.urls import path
from feghomeapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('intro/intro/', views.intro, name='intro'),
    path('intro/history/', views.history, name='history'), 
    path('intro/ogchart/', views.ogchart, name='ogchart'), 
    path('intro/sponsorship/', views.sponsorship, name='sponsorship'),     
    path('intro/access/', views.access, name='access'),            

    path('maintask/sea', views.sea, name='sea'),
    path('maintask/air', views.air, name='air'),   
    path('maintask/customs', views.customs, name='customs'),        
    
    
    path('fegsquare/fegsquare', views.fegsquare, name='fegsquare'),
    path('fegsquare/inquiry', views.inquiry, name='inquiry'),
        
    path('simfullo/', views.simfullo, name='simfullo'),
    path('travel/', views.travel, name='travel'),
]