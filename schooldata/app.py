# # import sqlite3

# # # Connect to the SQLite database
# # conn = sqlite3.connect('db.sqlite3')  # Replace 'your_database_name.db' with your actual database file name
# # cursor = conn.cursor()

# # # SQL command to insert unique data from StudentData to SchoolData
# # sql_command = """
# # INSERT INTO data_viz_schooldata (school_name)
# # SELECT DISTINCT school_name
# # FROM data_viz_studentdata;
# # """

# # # Execute the SQL command
# # cursor.execute(sql_command)

# # # Commit the transaction
# # conn.commit()

# # # Close the connection
# # conn.close()


# import sqlite3

# # Connect to the SQLite database
# conn = sqlite3.connect('db.sqlite3')  # Replace 'your_database_name.db' with your actual database file name
# cursor = conn.cursor()

# # Insert unique class names from StudentData into ClassData
# sql_class_command = """
# INSERT INTO data_viz_classdata (class_name)
# SELECT DISTINCT class_name
# FROM data_viz_studentdata;
# """
# cursor.execute(sql_class_command)

# # Insert unique awards from StudentData into AwardData
# sql_award_command = """
# INSERT INTO data_viz_awarddata (award)
# SELECT DISTINCT award
# FROM data_viz_studentdata;
# """
# cursor.execute(sql_award_command)

# # Insert unique assessment areas from StudentData into AssessmentAreaData
# sql_assessment_command = """
# INSERT INTO data_viz_assessmentareadata (assessment_areas)
# SELECT DISTINCT assessment_areas
# FROM data_viz_studentdata;
# """
# cursor.execute(sql_assessment_command)

# # Insert unique answers from StudentData into AnswerData
# sql_answer_command = """
# INSERT INTO data_viz_answerdata (answers)
# SELECT DISTINCT answers
# FROM data_viz_studentdata;
# """
# cursor.execute(sql_answer_command)

# # Insert unique subjects from StudentData into SubjectData
# sql_subject_command = """
# INSERT INTO data_viz_subjectdata (subject)
# SELECT DISTINCT subject
# FROM data_viz_studentdata;
# """
# cursor.execute(sql_subject_command)

# # Commit the transaction
# conn.commit()

# # Close the connection
# conn.close()


import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')  # Replace 'your_database_name.db' with your actual database file name
cursor = conn.cursor()

# Insert data into PeopleData from StudentData
sql_command = """
INSERT INTO data_viz_peopledata (student_id, first_name, last_name)
SELECT DISTINCT student_id, first_name, last_name
FROM data_viz_studentdata;
"""
cursor.execute(sql_command)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()


