from django.shortcuts import render
from .models import Squirrel
from django.http import HttpResponse

def map(request):
    squirrels=Squirrel.objects.all()[:50]
    context={
        'squirrels':squirrels,
    }
    return render(request, 'squirrel/map.html', context)

def all_squirrels(request):
    squirrel_list = Squirrel.objects.all()[:5]
    context = {'squirrel_list': squirrel_list}
    return render(request, 'squirrel/index.html', context)

