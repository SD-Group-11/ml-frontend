# Generated by Django 3.2 on 2021-09-28 09:53

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
                ('UserId', models.IntegerField()),
                ('filename', models.CharField(max_length=300)),
                ('model', models.CharField(default=None, max_length=300)),
                ('learningRate', models.CharField(max_length=300, null=True)),
                ('tol', models.CharField(max_length=300, null=True)),
                ('data', models.JSONField(default=dict)),
                ('testData', models.JSONField(default=dict)),
                ('nullValues', models.IntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'unique_together': {('UserId', 'filename', 'model')},
            },
        ),
    ]
