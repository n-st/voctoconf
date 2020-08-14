# Generated by Django 2.2.15 on 2020-08-14 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventpage', '0013_auto_20200814_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='bbb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='bbb.Room'),
        ),
        migrations.AlterField(
            model_name='event',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='eventpage.Room'),
        ),
    ]