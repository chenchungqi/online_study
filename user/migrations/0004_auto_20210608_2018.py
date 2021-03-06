# Generated by Django 2.2 on 2021-06-08 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_user_study_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cquestion_sum',
            field=models.IntegerField(default=0, verbose_name='正确题目数'),
        ),
        migrations.AddField(
            model_name='profile',
            name='grade_class',
            field=models.CharField(default='', max_length=20, verbose_name='年级'),
        ),
        migrations.AddField(
            model_name='profile',
            name='group_question_sum',
            field=models.IntegerField(default=0, verbose_name='题组数'),
        ),
        migrations.AddField(
            model_name='profile',
            name='question_difficulty',
            field=models.IntegerField(default=1, verbose_name='题目难度'),
        ),
        migrations.AddField(
            model_name='profile',
            name='question_num',
            field=models.IntegerField(default=0, verbose_name='做题总数'),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_time',
            field=models.IntegerField(default=0, verbose_name='做题时长（s）'),
        ),
        migrations.AddField(
            model_name='profile',
            name='wquestion_sum',
            field=models.IntegerField(default=0, verbose_name='错误题目数'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='', max_length=20, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_study_mode',
            field=models.CharField(default='0,0,0,0,0,0,0,0,0', max_length=20, verbose_name='用户学习模式'),
        ),
    ]
