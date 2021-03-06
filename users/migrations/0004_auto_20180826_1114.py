# Generated by Django 2.0.5 on 2018-08-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='refused_newsletters',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
