# Generated by Django 3.1.7 on 2021-04-26 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ui_apps', '0004_auto_20210426_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='name',
            new_name='version_number',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uiapps',
            name='platform',
            field=models.ManyToManyField(to='ui_apps.Platform'),
        ),
        migrations.RemoveField(
            model_name='uiapps',
            name='category',
        ),
        migrations.AddField(
            model_name='uiapps',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ui_apps.category'),
            preserve_default=False,
        ),
    ]
