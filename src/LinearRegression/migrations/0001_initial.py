# Generated by Django 3.2.7 on 2021-09-27 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.IntegerField()),
                ('filename', models.CharField(max_length=300)),
                ('Trained_coefficients', models.JSONField(default=dict, null=True)),
                ('meanSquaredError', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('TrainCoeffDetermination', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
                ('TestCoeffDetermination', models.DecimalField(decimal_places=10, max_digits=19, null=True)),
            ],
            options={
                'unique_together': {('UserId', 'filename')},
            },
        ),
    ]
