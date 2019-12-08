# Generated by Django 2.2.7 on 2019-12-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0004_auto_20191208_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Age',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], default='', help_text='Age', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Location',
            field=models.CharField(choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane')], default='', help_text='Location', max_length=100),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Running',
            field=models.BooleanField(default='', help_text='Running'),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='Shift',
            field=models.CharField(choices=[('PM', 'PM'), ('AM', 'AM')], default='', help_text='Shift', max_length=100),
        ),
    ]
