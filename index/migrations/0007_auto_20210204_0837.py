# Generated by Django 3.1.5 on 2021-02-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_fighter_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name (e.g. Club)', max_length=200)),
                ('damage', models.IntegerField(default=1, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='fighter',
            name='weapon',
            field=models.ManyToManyField(help_text='Select a language for this book', to='index.Weapon'),
        ),
    ]
