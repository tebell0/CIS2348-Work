# Tebello Rose - 2165470
import csv
majorslistfile = str(input('Input first csv file (including .csv extension)'))
majors = []
with open(majorslistfile, 'r', newline='') as MajorList:
    reader = csv.reader(MajorList)
    data = list(reader)
    majors.extend(data)
gpalistfile = str(input('Input second csv file (including .csv extension)'))
gpas = []
with open(gpalistfile, 'r', newline='') as GPAs:
    reader = csv.reader(GPAs)
    data = list(reader)
    gpas.extend(data)
graduationlistfile = str(input('Input third csv file (including .csv extension)'))
graddates = []
with open(graduationlistfile, 'r', newline='') as Grad:
    reader = csv.reader(Grad)
    data = list(reader)
    graddates.extend(data)

# The above code creates three different lists with all of the data from each of the csv files.
# This helps to ensure that student ID numbers are not duplicated.
all_data = []
student_info = {}
# The above creates an empty for future use and a dictionary to contain all student info
for id, lastname, firstname, major, da in majors:
    student_info[id] = {'Last Name': lastname, 'First Name': firstname, 'Major': major, 'DA': da}
# This initializes the dictionary with the values from the first list
for id, gpa in gpas:
    if id in student_info:
        student_info[id]['gpa'] = gpa
# This adds the gpa values to their corresponding student id
for id, graddate in graddates:
    if id in student_info:
        student_info[id]['Graduation Date'] = graddate
# This adds the graduation date values to the corresponding student id
for id, info in student_info.items():
    major = info['Major']
    first_name = info['First Name']
    last_name = info['Last Name']
    GPAverage = info.get('gpa', None)
    date = info.get("Graduation Date", None)
    DA = info.get("DA", None)
    all_data.append((id, major, first_name, last_name, GPAverage, date, DA))
# This puts all of the data together into a tuple with no duplications
def sort_key(x):
    return x[3]
all_data.sort(key=sort_key)
# This defines a function which is used to sort the list 'all_data' by the values at index 3 (the student's last name)
with open('FinalProjectFullRoster.csv', 'w', newline='') as newfile:
    writer = csv.writer(newfile)
    for row in all_data:
        writer.writerow(row)

# This completes question A of Final Project Part 1 by creating a csv file with the sorted student data

