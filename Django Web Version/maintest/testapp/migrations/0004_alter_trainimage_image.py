# Generated by Django 4.0.3 on 2022-04-04 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_trainimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainimage',
            name='image',
            field=models.ImageField(upload_to='media/train_images/'),
        ),
    ]
