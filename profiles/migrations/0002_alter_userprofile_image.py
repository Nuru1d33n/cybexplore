# Generated by Django 5.0.1 on 2024-02-09 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='static/assets/img/avatar.jpg', upload_to='profile_pics'),
        ),
    ]
