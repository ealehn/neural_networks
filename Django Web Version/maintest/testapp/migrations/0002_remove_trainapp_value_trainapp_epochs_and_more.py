# Generated by Django 4.0.3 on 2022-04-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainapp',
            name='value',
        ),
        migrations.AddField(
            model_name='trainapp',
            name='epochs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trainapp',
            name='hiddennodes',
            field=models.IntegerField(default=0),
        ),
    ]