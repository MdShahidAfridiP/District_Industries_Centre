# Generated by Django 3.0.8 on 2020-08-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0011_auto_20200803_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='g_policies',
            name='url',
        ),
        migrations.AddField(
            model_name='g_policies',
            name='document',
            field=models.FileField(default=1, upload_to='documents'),
            preserve_default=False,
        ),
    ]