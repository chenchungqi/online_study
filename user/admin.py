from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'nickname', 'lotteryCount', 'user_study_mode', 'email', 'is_staff', 'is_active', 'is_staff')

    def nickname(self, obj):
        return obj.profile.nickname

    def lotteryCount(self,obj):
        return obj.profile.lotteryCount

    def user_study_mode(self,obj):
        return obj.profile.user_study_mode


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'grade_class', 'question_difficulty', 'question_num', 'total_time', 'cquestion_sum', 'wquestion_sum', 'lotteryCount', 'user_study_mode')

