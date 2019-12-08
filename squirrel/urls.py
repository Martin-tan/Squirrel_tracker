from django.urls import path

from . import views

#generic view

app_name='squirrel'
urlpatterns=[
    path('map/',views.map,name='map'),
    path('<str:squirrel_id>/', views.squirrel_details),
]
