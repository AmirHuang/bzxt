# Generated by Django 2.0.2 on 2018-10-29 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='explosamplepeak',
            name='exploSampleFile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exploSamplePeak', to='samples.exploSampleFile', verbose_name='对应的炸药文件'),
        ),
        migrations.AddField(
            model_name='explosamplefile',
            name='exploSample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exploSampleFile', to='samples.exploSample', verbose_name='对应的炸药样本'),
        ),
        migrations.AddField(
            model_name='explosamplefile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员'),
        ),
        migrations.AddField(
            model_name='explosample',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员'),
        ),
        migrations.AddField(
            model_name='explochsample',
            name='exploSampleFile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exploChSample', to='samples.exploSampleFile', verbose_name='对应的炸药文件'),
        ),
        migrations.AddField(
            model_name='devshapesample',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员'),
        ),
        migrations.AddField(
            model_name='devcompsamplepeak',
            name='devCompSampleFile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devCompSamplePeak', to='samples.devCompSampleFile', verbose_name='对应的物证文件'),
        ),
        migrations.AddField(
            model_name='devcompsamplefile',
            name='devCompSample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devCompSampleFile', to='samples.devCompSample', verbose_name='对应的样本'),
        ),
        migrations.AddField(
            model_name='devcompsamplefile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员'),
        ),
        migrations.AddField(
            model_name='devcompsample',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='处理人员'),
        ),
        migrations.AddField(
            model_name='devcompchsample',
            name='devCompSampleFile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devCompChSample', to='samples.devCompSampleFile', verbose_name='对应的物证文件'),
        ),
    ]