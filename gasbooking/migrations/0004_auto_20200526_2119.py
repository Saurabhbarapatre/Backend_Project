# Generated by Django 2.2.6 on 2020-05-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gasbooking', '0003_auto_20200526_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newconnection',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
