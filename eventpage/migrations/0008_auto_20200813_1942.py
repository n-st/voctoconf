# Generated by Django 2.2.15 on 2020-08-13 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventpage', '0007_auto_20200813_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='evtype',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='evtype_modified',
            field=models.BooleanField(default=False),
        ),
    ]