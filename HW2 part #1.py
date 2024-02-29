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
print("Reading dates are from the input file:", input_filename)

while True:
    date_input = input()
    if date_input == '-1':
        break


    if valid_date(date_input):
        date = datetime.strptime(date_input, 'MM DD, YY')
        if date <= current_date:
            print(convert_format(date_input))
    else:
        print("Incorrect date format. Please enter dates in the format 'Month Day, Year'.")
