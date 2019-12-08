from django.core.management.base import BaseCommand
from squirrel.models import Squirrel
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', type = str)

    def handle(self, *args, **options):
        with open(options['path'], 'w') as fp:
            writer = csv.writer(fp, delimiter=',')
            values = list()
            variable_names = list()
            for f in Squirrel._meta.get_fields():
                values.append(f.name)
            for k in values[1:]:
                variable_names.append(Squirrel._meta.get_field(k).help_text)

            writer.writerow(variable_names)
            for j in range(len(Squirrel.objects.all())):
                row = list()
                for i in values:
                    if i == 'id': 
                        continue
                    row.append(getattr(Squirrel.objects.all()[j],i))
                writer.writerow(row)
        fp.close
