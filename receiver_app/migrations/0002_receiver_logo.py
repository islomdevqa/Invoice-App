# Generated by Django 4.0.5 on 2022-08-11 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiver_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='logo',
            field=models.ImageField(default='images/no_photo.png', upload_to=''),
        ),
    ]