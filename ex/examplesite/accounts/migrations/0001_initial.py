# Generated by Django 2.0.6 on 2018-06-23 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('grade', models.IntegerField()),
                ('school', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
    ]
