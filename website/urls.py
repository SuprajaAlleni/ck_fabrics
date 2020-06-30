from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index.html',views.index,name='index'),
    path('contact.html',views.contact,name='contact'),
    path('about.html',views.about,name='about'),
    path('medical.html',views.medical,name='medical'),
    path('filtration.html',views.filtration,name='filtration'),
    path('packaging.html',views.packaging,name='packaging'),
    path('agriculture.html',views.agriculture,name='agriculture'),
    path('health.html',views.health,name='health'),
    path('cosmetic.html',views.cosmetic,name='cosmetic'),
    path('mattress.html',views.mattress,name='mattress'),
    path('laminated.html',views.laminated,name='laminated'),
    path('melt_blown.html',views.melt,name='melt'),
    path('spunbond.html',views.spunbond,name='spunbond'),
]
