# Generated by Django 3.1.4 on 2020-12-20 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='emp_image1',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='emp_image2',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='emp_image3',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name1',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name2',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name3',
        ),
    ]