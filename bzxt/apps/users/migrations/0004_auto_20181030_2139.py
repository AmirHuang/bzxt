# Generated by Django 2.0.2 on 2018-10-30 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181029_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.IntegerField(choices=[(1, '超级管理员'), (2, '管理员'), (3, '普通用户')], default=3, help_text='权限标识', verbose_name='权限标识'),
        ),
    ]