# Generated by Django 3.1.7 on 2021-04-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui_apps', '0003_uiapps_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uiapps',
            name='category',
        ),
        migrations.AddField(
            model_name='uiapps',
            name='category',
            field=models.ManyToManyField(to='ui_apps.Category'),
        ),
    ]
