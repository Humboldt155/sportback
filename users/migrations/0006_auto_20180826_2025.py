# Generated by Django 2.0.5 on 2018-08-26 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180826_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='email'),
        ),
    ]
