print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}
print()
first = input('Select first service:')
print()
second = input('Select second service:')
print()
print()
print("Davy's auto shop invoice")
print()
if first == "-":
    first = 'No service'
    print(f'Service 1: {first}')
else: print(f'Service 1: {first}, ${services[first]}')
if second == '-':
    second = 'No service'
    print(f'Service 2: {second}')
else:
    print(f'Service 2: {second}, ${services[second]}')
print()
if first == 'No service':
    total = services[second]
elif second == 'No service':
    total = services[first]
else:
    total = services[first] + services[second]
print(f'Total: ${total}')
