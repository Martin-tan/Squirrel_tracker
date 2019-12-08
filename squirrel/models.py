from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    def __str__(self):
        return str(self.Unique_Squirrel_ID)

    Latitude = models.CharField(
        help_text = _('Latitude'),
        max_length = 100,
        default = ''
    ) 
    Longitude = models.CharField( 
        help_text = _('Longitude'),
        max_length = 100,
        default = ''
    ) 
    Unique_Squirrel_ID = models.CharField( 
        primary_key = True,
        help_text = _('Unique_Squirrel_ID'), 
        max_length = 100,
        default = ''
    ) 
    PM = 'PM'
    AM = 'AM'
    shift_choices = (
            (PM,'PM'),
            (AM,'AM'),
            )

    Shift = models.CharField( 
        help_text = _('Shift'),
        choices = shift_choices,
        max_length = 100,
        default = ''
    ) 
    Date = models.CharField( 
        help_text = _('Date'), 
        max_length = 100,
        default = ''
    ) 
    adult = 'Adult'
    juvenile = 'Juvenile'
    age_choices = (
            (adult, 'Adult'),
            (juvenile, 'Juvenile'),
            )
    Age = models.CharField( 
        help_text = _('Age'),
        choices = age_choices,
        max_length = 100, 
        default = ''
    ) 
    Primary_Fur_Color = models.CharField( 
        help_text = _('Primary_Fur_Color'), 
        max_length = 100, 
        default = ''
    ) 
    above_ground = 'Above Ground'
    ground_plane = 'Ground Plane'
    location_choices = (
            (above_ground, 'Above Ground'),
            (ground_plane, 'Ground Plane'),
            )
    Location = models.CharField(
        help_text = _('Location'),
        choices = location_choices,
        max_length = 100, 
        default = ''
    ) 
    Specific_Location = models.CharField( 
        help_text = _('Specific_Location'), 
        max_length = 100, 
        default = ''
    )
    Running = models.BooleanField(
        help_text = _('Running'),
        default = ''
    )
    Chasing = models.BooleanField (
        help_text = _('Chasing'),
        default = ''
    )
    Climbing = models.BooleanField (
        help_text = _('Climbing'),
        default = ''
   )
    Eating = models.BooleanField (
        help_text = _('Eating'),
        default = ''
    )
    Foraging = models.BooleanField (
        help_text = _('Foraging'),
        default = ''
    )
    Other_Activities = models.CharField (
        help_text = _('Other_Activities'),
        max_length = 100,
        default = ''
    )
    Kuks = models.BooleanField (
        help_text = _('Kuks'),
        default = ''
    )
    Quaas = models.BooleanField (
        help_text = _('Quaas'),
        default = ''
    )
    Moans = models.BooleanField (
        help_text = _('Moans'),
        default = ''
    )
    Tail_flags = models.BooleanField (
        help_text = _('Tail_flags'),
        default = ''
    )
    Tail_twitches = models.BooleanField (
        help_text = _('Tail_twitches'),
        default = ''
    )
    Approaches = models.BooleanField (
        help_text = _('Approaches'),
        default = ''
    )
    Indifferent = models.BooleanField (
        help_text = _('Indifferent'),
        default = ''
    )
    Runs_from = models.BooleanField (
        help_text = _('Runs_from'),
        default = ''
    )

