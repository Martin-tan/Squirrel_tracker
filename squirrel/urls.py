from django.urls import path

from . import views

#generic view

app_name='squirrel'
urlpatterns=[
    path('', views.all_squirrels),
    path('map/',views.map,name='map'),
]
