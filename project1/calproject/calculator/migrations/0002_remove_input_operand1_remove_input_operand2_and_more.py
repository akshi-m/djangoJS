# Generated by Django 4.0.6 on 2022-07-18 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='operand1',
        ),
        migrations.RemoveField(
            model_name='input',
            name='operand2',
        ),
        migrations.RemoveField(
            model_name='input',
            name='result',
        ),
    ]
