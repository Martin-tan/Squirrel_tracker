from django.shortcuts import render
from .models import Squirrel
from django.http import HttpResponse
from django.http import Http404

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

def squirrel_details(request, squirrel_id):
    try:         #squirrel not found
        squirrel = Squirrel.objects.get(Unique_Squirrel_ID = squirrel_id)
        delete = request.POST.get('Delete')
        update = request.POST.get('Update')
        if delete == 'delete':
            squirrel.delete()
        if update == 'update':
            squirrel.Latitude = request.POST.get('Latitude')
            squirrel.Longitude = request.POST.get('Longitude')
            id = request.POST.get('Unique_Squirrel_ID')
            if id in [i.Unique_Squirrel_ID for i in Squirrel.objects.all()]:
                raise Http404("UNIQUE ID CONSTRAINT failed!")
            else:
                squirrel.Unique_Squirrel_ID = id
            squirrel.Shift = request.POST.get('Shift')
            squirrel.Date = request.POST.get('Date')
            squirrel.Age = request.POST.get('Age')
            squirrel.Primary_Fur_Color = request.POST.get('Primary_Fur_Color')
            squirrel.Location = request.POST.get('Location')
            squirrel.Specific_Location = request.POST.get('Specific_Location')
            squirrel.Running = request.POST.get('Running')
            squirrel.Chasing = request.POST.get('Chasing')
            squirrel.Unique_Squirrel_ID = request.POST.get('Unique_Squirrel_ID')
            squirrel.Climbing = request.POST.get('Climbing')
            squirrel.Eating = request.POST.get('Eating')
            squirrel.Foraging = request.POST.get('Foraging')
            squirrel.Other_Activities = request.POST.get('Other_Activities')
            squirrel.Kuks = request.POST.get('Kuks')
            squirrel.Quaas = request.POST.get('Quaas')
            squirrel.Moans = request.POST.get('Moans')
            squirrel.Tail_flags = request.POST.get('Tail_flags')
            squirrel.Tail_twitches = request.POST.get('Tail_twitches')
            squirrel.Approaches = request.POST.get('Approaches')
            squirrel.Indifferent = request.POST.get('Indifferent')
            squirrel.Runs_from = request.POST.get('Runs_from')
            squirrel.save()
        return render(request, 'squirrel/detail.html',{'squirrel':squirrel})
    except Squirrel.DoesNotExist:
        raise Http404("Squirrel does not exist")

