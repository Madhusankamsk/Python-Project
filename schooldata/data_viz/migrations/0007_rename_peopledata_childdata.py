# Generated by Django 5.0.1 on 2024-02-07 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_viz', '0006_peopledata'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PeopleData',
            new_name='ChildData',
        ),
    ]
