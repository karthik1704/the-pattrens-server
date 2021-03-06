# Generated by Django 3.1.7 on 2021-04-26 15:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_requests', '0003_auto_20210225_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userrequest',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrequest',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='app_url',
            field=models.URLField(verbose_name='App URL/ Website URL'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Why do you love this app?'),
        ),
        migrations.AlterField(
            model_name='userrequest',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Your Name'),
        ),
    ]
