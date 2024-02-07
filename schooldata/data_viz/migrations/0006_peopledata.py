# Generated by Django 5.0.1 on 2024-02-07 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_viz', '0005_answerdata_assessmentareadata_awarddata_classdata_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_id', models.CharField(max_length=100, verbose_name='Student ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
            ],
        ),
    ]
