# Generated by Django 3.2.7 on 2021-09-27 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NaiveBayes', '0002_alter_naivebayes_testingaccuracy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='naivebayes',
            name='TrainingAccuracy',
        ),
    ]
