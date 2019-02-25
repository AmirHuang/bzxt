# _*_ coding: utf-8 _*_
# @Time     : 19:23
# @Author   : Amir
# @Site     : 
# @File     : serializers.py
# @Software : PyCharm

import re
from rest_framework import serializers
from datetime import datetime
from datetime import timedelta
from rest_framework.validators import UniqueValidator

from .models import UserProfile


class UserDetailSerializer(serializers.ModelSerializer):
    # 用户详情序列化
    class Meta:
        model = UserProfile
        fields = ("username", "name", 'userID', "gender", "role", "phone", "isDelete", "picUrl", "note")


class UserReSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label='姓名', help_text='姓名', required=True,
                                     allow_blank=False,
                                     validators=[UniqueValidator(queryset=UserProfile.objects.all(),
                                                                 message='该姓名已存在')])
    password = serializers.CharField(style={'input_type': 'password'},
                                     help_text='密码', label='密码')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        validated_data["password"] = instance.password
        return super().update(instance, validated_data)

    # def update(self, instance, validated_data):
    #     from django.contrib.auth.hashers import make_password
    #     validated_data['password'] = make_password(validated_data['password'])
    #     return super().update(instance, validated_data)

    def validate_role(self, role):
        # 注意参数，self以及字段名
        # 注意函数名写法，validate_ + 字段名

        if not self.context['request'].user.is_anonymous:
            if self.context['request'].user.role == 3 and role < 3:
                raise serializers.ValidationError('您没有这个权限')
            elif self.context['request'].user.role == 2 and role < 2:
                raise serializers.ValidationError('您没有这个权限')
            else:
                return role
        else:
            if role != 3:
                raise serializers.ValidationError('您没有这个权限')
            return role

    class Meta:
        model = UserProfile
        fields = ("username", "password", "userID", "name", "gender", "role", "phone", "picUrl", "note")
