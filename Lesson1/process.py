# For reading the data from csv file

import unicodecsv

def readcsv(filename):
	with open(filename,"rb") as f:
		reader = unicodecsv.DictReader(f);
		return list(reader);

enrollments = readcsv('enrollments.csv');    
daily_engagement = readcsv('daily_engagement.csv');
project_submissions = readcsv('project_submissions.csv');

print enrollments
# For investigation the data

from sets import Set

def count_unique(list_name):
	SET = Set([]);
	
students_id = Set([]);
for each in enrollments:
	students_id.add(each['account_key']);
no_of_students = len(students_id);

rows_enrollments = len(enrollments);
rows_daily_engagement = len(daily_engagement);
rows_project_submissions = len(project_submissions);
