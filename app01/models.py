from django.db import models

# Create your models here.


class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32)
    ctime = models.DateTimeField(auto_now_add=True, null=True)
    uptime = models.DateTimeField(auto_now=True, null=True)


class UserInfoEX(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=60)
    email = models.CharField(max_length=60, null=True)
    test = models.EmailField(max_length=19, null=True)
    user_type_choices = (
        (1, '超级用户'),
        (2, '普通用户'),
        (3, '低端用户'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices, default=1)
    user_group = models.ForeignKey('UserGroup', to_field='uid', default=1, on_delete=models.CASCADE)