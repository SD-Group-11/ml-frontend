# Generated by Django 3.2 on 2021-05-22 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Userid', models.IntegerField()),
                ('filename', models.CharField(max_length=300)),
                ('data', models.JSONField(default=dict)),
            ],
        ),
    ]