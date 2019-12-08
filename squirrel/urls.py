from django.urls import path

from . import views

app_name='squirrel'
urlpatterns=[
    path('', views.all_squirrels),
    path('map/',views.map,name='map'),
    path('add/', views.add_squirrels),
    path('stats/', views.squirrel_stats),
    path('<str:squirrel_id>/', views.squirrel_details),
]
