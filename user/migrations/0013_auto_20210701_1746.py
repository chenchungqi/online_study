# Generated by Django 2.2 on 2021-07-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20210701_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='achievement_title',
            field=models.CharField(default='暂无', max_length=100, verbose_name='成就'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lottery_model',
            field=models.CharField(default='暂无', max_length=200, verbose_name='抽奖模型'),
        ),
    ]
