from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, verbose_name='昵称', default='')
    lotteryCount = models.IntegerField(verbose_name='可抽奖次数', default=0)
    user_study_mode = models.CharField(max_length=20, verbose_name='用户学习模式', default='0,0,0,0,0,0,0,0,0')

    grade_class = models.CharField(max_length=20, verbose_name='年级', default='')
    question_difficulty = models.IntegerField(verbose_name='题目难度', default=0)
    question_num = models.IntegerField(verbose_name='做题总数', default=0)
    total_time = models.IntegerField(verbose_name='做题时长（s）', default=0)
    group_question_sum = models.IntegerField(verbose_name='题组数', default=0)
    cquestion_sum = models.IntegerField(verbose_name='正确题目数', default=0)
    wquestion_sum = models.IntegerField(verbose_name='错误题目数', default=0)
    achievement_title = models.CharField(max_length=100, verbose_name='成就', default='')

    def __str__(self):
        return '<Profile: %s %s for %s>' % (self.nickname, self.lotteryCount, self.user.username)


def get_nickname(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return ''


def get_nickname_or_username(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return self.username


def has_nickname(self):
    return Profile.objects.filter(user=self).exists()


def display_time_diff(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        seconds = profile.total_time/1000
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        display_time = "%02d小时:%02d分钟:%02d秒" % (h, m, s)
        return display_time
    else:
        return ''




User.get_nickname = get_nickname
User.get_nickname_or_username = get_nickname_or_username
User.has_nickname = has_nickname
User.display_time_diff = display_time_diff
