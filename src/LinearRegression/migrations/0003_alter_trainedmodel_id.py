# Generated by Django 3.2.7 on 2021-09-25 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LinearRegression', '0002_auto_20210922_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainedmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
