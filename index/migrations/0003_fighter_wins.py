# Generated by Django 3.1.5 on 2021-02-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_zombie'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='wins',
            field=models.IntegerField(null=True),
        ),
    ]
