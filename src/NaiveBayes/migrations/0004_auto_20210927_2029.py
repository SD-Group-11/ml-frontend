# Generated by Django 3.2.7 on 2021-09-27 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NaiveBayes', '0003_remove_naivebayes_trainingaccuracy'),
    ]

    operations = [
        migrations.CreateModel(
            name='NBTrainedModel',
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
        migrations.DeleteModel(
            name='NaiveBayes',
        ),
    ]
