import datetime

def valid_date(date_str):
    parts = date_str.split()
    if len(parts) != 3:
        return False
    else:
        return True
    parts = [month, day, years]
    months = ['January', 'February', 'March', 'April', "May", 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    if month not in months:
        return False
    elif not day[:-1].isdigit():
        return False
    elif not year.isdigit():
        return False
    else:
        return True

def convert_format(date_str):
    date = datetime.strptime(date_str, 'MM DD, YY')
    return '{}/{}/{}'.format(date.month, date.day, date.year)

current_date = datetime.now()
input_filename = "inputDates.txt"
output_filename = 'parsedDates.txt'

print("Reading dates from the input file: ", input_filename)
parsedDates = []

with open(input_filename, 'r') as input_file:
    for line in input_file:
        date_input = line.strip()

    if date_input == '-1':
        False

    if valid_date(date_input):
        date = datetime.strptime(date_input, "MM DD, YY")
        if date <= current_date:
            parsedDates.append(convert_format(date_input))
        else:
            print('Incorrect date format in the input file:', date_input)

print("Writing  parsed dates to the output files: ", output_filename)

with open(output_filename, 'w') as output_file:
    for date in parsedDates:
        output_file.write(date +'\n')
print("Parsing and writing completed.")