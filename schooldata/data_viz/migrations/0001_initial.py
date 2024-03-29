# Generated by Django 5.0.1 on 2024-02-04 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('student_id', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('year_level', models.IntegerField()),
                ('class_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('answers', models.CharField(max_length=100)),
                ('correct_answers', models.IntegerField()),
                ('question_number', models.IntegerField()),
                ('subject_contents', models.CharField(max_length=255)),
                ('assessment_areas', models.CharField(max_length=255)),
                ('sydney_correct_count_percentage', models.FloatField()),
                ('sydney_average_score', models.FloatField()),
                ('sydney_participants', models.IntegerField()),
                ('student_score', models.FloatField()),
                ('student_total_assessed', models.FloatField()),
                ('student_area_assessed_score', models.FloatField()),
                ('total_area_assessed_score', models.FloatField()),
                ('participant', models.IntegerField()),
                ('correct_answer_percentage_per_class', models.FloatField()),
                ('average_score', models.FloatField()),
                ('school_percentile', models.FloatField()),
                ('sydney_percentile', models.FloatField()),
                ('strength_status', models.CharField(max_length=100)),
                ('high_distinct_count', models.IntegerField()),
                ('distinct_count', models.IntegerField()),
                ('credit_count', models.IntegerField()),
                ('participant_count', models.IntegerField()),
                ('award', models.CharField(max_length=100)),
            ],
        ),
    ]
