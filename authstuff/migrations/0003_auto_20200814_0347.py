# Generated by Django 2.2.15 on 2020-08-14 01:47

import authstuff.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authstuff', '0002_authtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtoken',
            name='token',
            field=models.CharField(default=authstuff.models.generate_token, max_length=42, validators=[authstuff.models.validate_token]),
        ),
    ]
