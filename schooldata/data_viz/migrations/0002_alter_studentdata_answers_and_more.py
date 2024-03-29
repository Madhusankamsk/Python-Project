# Generated by Django 5.0.1 on 2024-02-04 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_viz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='answers',
            field=models.CharField(max_length=100, verbose_name='Answers'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='assessment_areas',
            field=models.CharField(max_length=255, verbose_name='Assessment Areas'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='average_score',
            field=models.FloatField(verbose_name='Average Score'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='award',
            field=models.CharField(max_length=100, verbose_name='Award'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='class_name',
            field=models.CharField(max_length=100, verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='correct_answer_percentage_per_class',
            field=models.FloatField(verbose_name='Correct Answer Percentage Per Class'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='correct_answers',
            field=models.IntegerField(verbose_name='Correct Answers'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='credit_count',
            field=models.IntegerField(verbose_name='Credit Count'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='distinct_count',
            field=models.IntegerField(verbose_name='Distinct Count'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='high_distinct_count',
            field=models.IntegerField(verbose_name='High Distinct Count'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='participant',
            field=models.IntegerField(verbose_name='Participant'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='participant_count',
            field=models.IntegerField(verbose_name='Participant Count'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='question_number',
            field=models.IntegerField(verbose_name='Question Number'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='school_name',
            field=models.CharField(max_length=255, verbose_name='School Name'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='school_percentile',
            field=models.FloatField(verbose_name='School Percentile'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='strength_status',
            field=models.CharField(max_length=100, verbose_name='Strength Status'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='student_area_assessed_score',
            field=models.FloatField(verbose_name='Student Area Assessed Score'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='student_id',
            field=models.CharField(max_length=100, verbose_name='Student ID'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='student_score',
            field=models.FloatField(verbose_name='Student Score'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='student_total_assessed',
            field=models.FloatField(verbose_name='Student Total Assessed'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='subject',
            field=models.CharField(max_length=100, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='subject_contents',
            field=models.CharField(max_length=255, verbose_name='Subject Contents'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='sydney_average_score',
            field=models.FloatField(verbose_name='Sydney Average Score'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='sydney_correct_count_percentage',
            field=models.FloatField(verbose_name='Sydney Correct Count Percentage'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='sydney_participants',
            field=models.IntegerField(verbose_name='Sydney Participants'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='sydney_percentile',
            field=models.FloatField(verbose_name='Sydney Percentile'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='total_area_assessed_score',
            field=models.FloatField(verbose_name='Total Area Assessed Score'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='year',
            field=models.IntegerField(verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='studentdata',
            name='year_level',
            field=models.IntegerField(verbose_name='Year Level'),
        ),
    ]
