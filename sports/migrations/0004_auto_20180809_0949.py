# Generated by Django 2.0.5 on 2018-08-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_auto_20180808_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsubgroup',
            name='sports',
            field=models.ManyToManyField(related_name='sport_sub_groups', to='sports.Sport'),
        ),
    ]
