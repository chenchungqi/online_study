from django.db import models
from django.contrib.auth.models import User


class thingsget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    achievement_time1 = models.IntegerField(default=0)
    achievement_time2 = models.BooleanField(default=False)
    achievement_time3 = models.BooleanField(default=False)
    achievement_time4 = models.BooleanField(default=False)
    achievement_time5 = models.BooleanField(default=False)
    achievement_time6 = models.BooleanField(default=False)
    achievement_time7 = models.BooleanField(default=False)

    def __str__(self):
        return '<things: %s %s for %s>' % (self.achievement_time1, self.achievement_time2, self.achievement_time3)

