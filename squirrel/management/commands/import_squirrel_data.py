from django.core.management.base import BaseCommand
from squirrel.models import Squirrel 
import pandas as pd

class Command(BaseCommand):   

    def add_arguments(self, parser):
        parser.add_argument('file',nargs=1,type=str)

    def handle(self, *args, **options):
        file = pd.read_csv(options['file'][0])
        for index, row in file.iterrows():
            Squirrel.objects.create(
                Longitude = row['Y'],
                Latitude = row['X'],
                Unique_Squirrel_ID = row['Unique Squirrel ID'],
                Shift = row['Shift'],
                Date = row['Date'],
                Age = row['Age'],
                Primary_Fur_Color = row['Primary Fur Color'],
                Location = row['Location'],
                Specific_Location = row['Specific Location'],
                Running = row['Running'],
                Chasing = row['Chasing'],
                Climbing = row['Climbing'],
                Eating = row['Eating'],
                Foraging = row['Foraging'],
                Other_Activities = row['Other Activities'],
                Kuks = row['Kuks'],
                Quaas = row['Quaas'],
                Moans = row['Moans'],
                Tail_flags = row['Tail flags'],
                Tail_twitches = row['Tail twitches'],
                Approaches = row['Approaches'],
                Indifferent = row['Indifferent'],
                Runs_from = row['Runs from'],
            )

