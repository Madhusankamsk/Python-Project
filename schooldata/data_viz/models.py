from django.db import models
from django.utils.translation import gettext_lazy as _

class StudentData(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(_("School Name"), max_length=255)
    year = models.IntegerField(_("Year"))
    student_id = models.CharField(_("Student ID"), max_length=100)
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    year_level = models.IntegerField(_("Year Level"))
    class_name = models.CharField(_("Class"), max_length=100)
    subject = models.CharField(_("Subject"), max_length=100)
    answers = models.CharField(_("Answers"), max_length=100)
    correct_answers = models.IntegerField(_("Correct Answers"))
    question_number = models.IntegerField(_("Question Number"))
    subject_contents = models.CharField(_("Subject Contents"), max_length=255)
    assessment_areas = models.CharField(_("Assessment Areas"), max_length=255)
    sydney_correct_count_percentage = models.FloatField(_("Sydney Correct Count Percentage"))
    sydney_average_score = models.FloatField(_("Sydney Average Score"))
    sydney_participants = models.IntegerField(_("Sydney Participants"))
    student_score = models.FloatField(_("Student Score"))
    student_total_assessed = models.FloatField(_("Student Total Assessed"))
    student_area_assessed_score = models.FloatField(_("Student Area Assessed Score"))
    total_area_assessed_score = models.FloatField(_("Total Area Assessed Score"))
    participant = models.IntegerField(_("Participant"))
    correct_answer_percentage_per_class = models.FloatField(_("Correct Answer Percentage Per Class"))
    average_score = models.FloatField(_("Average Score"))
    school_percentile = models.FloatField(_("School Percentile"))
    sydney_percentile = models.FloatField(_("Sydney Percentile"))
    strength_status = models.CharField(_("Strength Status"), max_length=100)
    high_distinct_count = models.IntegerField(_("High Distinct Count"))
    distinct_count = models.IntegerField(_("Distinct Count"))
    credit_count = models.IntegerField(_("Credit Count"))
    participant_count = models.IntegerField(_("Participant Count"))
    award = models.CharField(_("Award"), max_length=100)

# class AllData(models.Model):
#     student_id = models.CharField(_("Student ID"), max_length=100)
#     first_name = models.CharField(_("First Name"), max_length=100)
#     last_name = models.CharField(_("Last Name"), max_length=100)

class SchoolData(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(_("School Name"), max_length=255)
   
class ClassData(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(_("Class Name"), max_length=255)
    
class AwardData(models.Model):
    id = models.AutoField(primary_key=True)
    award = models.CharField(_("Award"), max_length=255)

class AssessmentAreaData(models.Model):
    id = models.AutoField(primary_key=True)
    assessment_areas = models.CharField(_("Assessment Areas"), max_length=255)


class AnswerData(models.Model):
    id = models.AutoField(primary_key=True)
    answers = models.CharField(_("Answers"), max_length=255)

class SubjectData(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(_("Subject"), max_length=255)


