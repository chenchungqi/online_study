# Generated by Django 2.2 on 2021-06-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_profile_achievement_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='diamond',
            field=models.IntegerField(default=0, verbose_name='钻石'),
        ),
    ]
