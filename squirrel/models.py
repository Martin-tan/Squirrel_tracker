from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    def __str__(self):
        return str(self.Unique_Squirrel_ID)

    Latitude = models.FloatField(
        help_text = _('Latitude'),
        default = ''
    ) 
    Longitude = models.FloatField( 
        help_text = _('Longitude'),
        default = ''
    ) 
    Unique_Squirrel_ID = models.CharField( 
        primary_key = True,
        help_text = _('Unique_Squirrel_ID'), 
        max_length = 100,
        default = ''
    ) 
    Shift = models.CharField( 
        help_text = _('Shift'),
        max_length = 100,
        default = ''
    ) 
    Date = models.CharField( 
        help_text = _('Date'), 
        max_length = 100,
        default = ''
    ) 
    Age = models.CharField( 
        help_text = _('Age'), 
        max_length = 100, 
        default = ''
    ) 
    Primary_Fur_Color = models.CharField( 
        help_text = _('Primary_Fur_Color'), 
        max_length = 100, 
        default = ''
    ) 
    Location = models.CharField(
        help_text = _('Location'),
        max_length = 100, 
        default = ''
    ) 
    Specific_Location = models.CharField( 
        help_text = _('Specific_Location'), 
        max_length = 100, 
        default = ''
    )
    Running = models.NullBooleanField(
        help_text = _('Running'),
        max_length = 100,
        default = ''
    )
    Chasing = models.NullBooleanField(
        help_text = _('Chasing'),
        max_length = 100,
        default = ''
    )
    Climbing = models.NullBooleanField(
        help_text = _('Climbing'),
        max_length = 100,
        default = ''
    )
    Eating = models.NullBooleanField(
        help_text = _('Eating'),
        max_length = 100,
        default = ''
    )
    Foraging = models.NullBooleanField(
        help_text = _('Foraging'),
        max_length = 100,
        default = ''
    )
    Other_Activities = models.CharField(
        help_text = _('Other_Activities'),
        max_length = 100,
        default = ''
    )
    Kuks = models.NullBooleanField(
        help_text = _('Kuks'),
        max_length = 100,
        default = ''
    )
    Quaas = models.NullBooleanField(
        help_text = _('Quaas'),
        max_length = 100,
        default = ''
    )
    Moans = models.NullBooleanField(
        help_text = _('Moans'),
        max_length = 100,
        default = ''
    )
    Tail_flags = models.NullBooleanField(
        help_text = _('Tail_flags'),
        max_length = 100,
        default = ''
    )
    Tail_twitches = models.NullBooleanField(
        help_text = _('Tail_twitches'),
        max_length = 100,
        default = ''
    )
    Approaches = models.NullBooleanField(
        help_text = _('Approaches'),
        max_length = 100,
        default = ''
    )
    Indifferent = models.NullBooleanField(
        help_text = _('Indifferent'),
        max_length = 100,
        default = ''
    )
    Runs_from = models.NullBooleanField(
        help_text = _('Runs_from'),
        max_length = 100,
        default = ''
    )

