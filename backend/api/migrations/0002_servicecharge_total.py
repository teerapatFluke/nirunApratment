# Generated by Django 3.1.2 on 2020-10-30 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecharge',
            name='total',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
