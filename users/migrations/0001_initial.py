# Generated by Django 3.1.5 on 2021-02-03 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0003_fighter_wins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('fighter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='index.fighter')),
            ],
        ),
    ]
