# Generated by Django 2.2.2 on 2020-05-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gasbooking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newconnection',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
