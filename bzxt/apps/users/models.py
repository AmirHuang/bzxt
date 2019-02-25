from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    # 用户
    ROLE_TYPE = (
        (1, '超级管理员'),
        (2, '管理员'),
        (3, '普通用户'),
    )
    GENDER = (
        ('male', '男'),
        ('female', '女'),
    )
    userID = models.CharField('人员编号', max_length=20)
    name = models.CharField('人员姓名', max_length=6)
    gender = models.CharField('性别', max_length=6, choices=GENDER, default='female')
    phone = models.CharField('联系电话', max_length=20)
    isDelete = models.BooleanField('是否逻辑删除', default=False)
    role = models.IntegerField('权限标识', help_text='权限标识', choices=ROLE_TYPE, default=3)
    picUrl = models.ImageField('头像路径', max_length=100, upload_to="image/user/", null=True, blank=True)
    note = models.CharField('备注', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name