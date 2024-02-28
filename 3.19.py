import math
height = float(input('Enter wall height (feet):'))
print()
width = float(input('Enter wall width (feet):'))
print()
area = int(height * width)
print('Wall area:', area, 'square feet')
paint = float(area / 350)
print('Paint needed:', f'{paint:.2f} gallons')
cans = int(math.ceil(paint))
print('Cans needed:', cans, 'can(s)')
print()
color = input("Choose a color to paint the wall:")
print()
if color == "blue":
    cost = cans * 25
elif color == 'red':
    cost = cans * 35
else:
    cost = cans * 23
print(f'Cost of purchasing', color, f'paint: ${cost}')
