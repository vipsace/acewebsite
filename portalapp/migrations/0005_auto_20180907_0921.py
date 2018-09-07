# Generated by Django 2.1.1 on 2018-09-07 03:51

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0010_auto_20180414_2058'),
        ('portalapp', '0004_auto_20180815_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='aceuserprofile',
            name='is_council',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aceuserprofile',
            name='picture',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_picture', to='filer.File'),
        ),
    ]
