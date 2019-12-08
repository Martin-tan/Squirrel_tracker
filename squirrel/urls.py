from django.urls import path, include

from . import views

app_name = 'squirrel'
urlpatterns = [
    path('', views.all_squirrels),
    path('add/',views.add_squirrels),
    path('stats/',views.squirrel_stats),
    path('map/',views.map),
    path('<squirrel_id>/', views.squirrel_details),
    
]
