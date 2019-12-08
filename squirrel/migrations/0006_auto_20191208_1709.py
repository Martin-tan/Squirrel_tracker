# Generated by Django 2.2.7 on 2019-12-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0005_auto_20191208_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Approaches',
            field=models.BooleanField(default='', help_text='Approaches'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Chasing',
            field=models.BooleanField(default='', help_text='Chasing'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Climbing',
            field=models.BooleanField(default='', help_text='Climbing'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Eating',
            field=models.BooleanField(default='', help_text='Eating'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Foraging',
            field=models.BooleanField(default='', help_text='Foraging'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Indifferent',
            field=models.BooleanField(default='', help_text='Indifferent'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Kuks',
            field=models.BooleanField(default='', help_text='Kuks'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Moans',
            field=models.BooleanField(default='', help_text='Moans'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Other_Activities',
            field=models.BooleanField(default='', help_text='Other_Activities'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Quaas',
            field=models.BooleanField(default='', help_text='Quaas'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Runs_from',
            field=models.BooleanField(default='', help_text='Runs_from'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Tail_flags',
            field=models.BooleanField(default='', help_text='Tail_flags'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Tail_twitches',
            field=models.BooleanField(default='', help_text='Tail_twitches'),
        ),
    ]
