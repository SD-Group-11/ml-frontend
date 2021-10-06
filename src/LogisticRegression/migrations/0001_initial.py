# Generated by Django 3.2.7 on 2021-10-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogisticTrainedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.IntegerField()),
                ('filename', models.CharField(max_length=300)),
                ('TrainingAccuracy', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('f1score', models.JSONField(default=dict, null=True)),
                ('AUCScore', models.JSONField(default=dict, null=True)),
                ('TestingAccuracy', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
            ],
            options={
                'unique_together': {('UserId', 'filename')},
            },
        ),
    ]
