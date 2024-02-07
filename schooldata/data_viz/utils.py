import csv
from .models import StudentData


def load_student_data():
    with open('student_data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = StudentData.objects.get_or_create(
                school_name=row[0],
                year=row[1],
                student_id=row[2],
                first_name=row[3],
                last_name=row[4],
                year_level=row[5],
                class_name=row[6],
                subject=row[7],
                answers=row[8],
                correct_answers=row[9],
                question_number=row[10],
                subject_contents=row[11],
                assessment_areas=row[12],
                sydney_correct_count_percentage=row[13],
                sydney_average_score=row[14],
                sydney_participants=row[15],
                student_score=row[16],
                student_total_assessed=row[17],
                student_area_assessed_score=row[18],
                total_area_assessed_score=row[19],
                participant=row[20],
                correct_answer_percentage_per_class=row[21],
                average_score=row[22],
                school_percentile=row[23],
                sydney_percentile=row[24],
                strength_status=row[25],
                high_distinct_count=row[26],
                distinct_count=row[27],
                credit_count=row[28],
                participant_count=row[29],
                award=row[30]
            )

