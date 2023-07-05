from django.urls import path
from feghomeapp_jp import views

urlpatterns = [
    path('', views.home_jp, name='home_jp'),
    path('intro/intro_jp/', views.intro_jp, name='intro_jp'),
    path('intro/history_jp/', views.history_jp, name='history_jp'), 
    path('intro/ogchart_jp/', views.ogchart_jp, name='ogchart_jp'), 
    path('intro/sponsorship_jp/', views.sponsorship_jp, name='sponsorship_jp'),     
    path('intro/access_jp/', views.access_jp, name='access_jp'),            

    path('maintask/sea_jp', views.sea_jp, name='sea_jp'),
    path('maintask/air_jp', views.air_jp, name='air_jp'),   
    path('maintask/customs_jp', views.customs_jp, name='customs_jp'),        
    

    path('corevalue_jp/corevalue_jp', views.corevalue_jp, name='corevalue_jp'),
    path('corevalue_jp/rational_price_jp', views.rational_price_jp, name='rational_price_jp'),
        
    path('simfullo_jp/', views.simfullo_jp, name='simfullo_jp'),
    path('travel_jp/', views.travel_jp, name='travel_jp'),
    path('inquiry_jp/', views.inquiry_jp, name='inquiry_jp'),
]