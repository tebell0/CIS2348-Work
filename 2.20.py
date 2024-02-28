lemon = float(input('Enter amount of lemon juice (in cups):'))
print()
water = float(input('Enter amount of water (in cups):'))
print()
agave = float(input('Enter amount of agave nectar (in cups):'))
print()
servings = float(input('How many servings does this make?'))
print()
print()
print('Lemonade ingredients - yields', f'{servings:.2f} servings')
print(f'{lemon:.2f} cup(s) lemon juice')
print(f'{water:.2f} cup(s) water')
print(f'{agave:.2f} cup(s) agave nectar')
print()
count= float(input('How many servings would you like to make?'))
print()
print()
parameter = count / servings
lemon2= lemon * parameter
water2 = water * parameter
agave2 = agave * parameter
print('Lemonade ingredients - yields', f'{count:.2f} servings')
print(f'{lemon2:.2f} cup(s) lemon juice')
print(f'{water2:.2f} cup(s) water')
print(f'{agave2:.2f} cup(s) agave nectar')
print()
lemon3 = lemon2/16
water3 = water2/16
agave3 = agave2/16
print('Lemonade ingredients - yields', f'{count:.2f} servings')
print(f'{lemon3:.2f} gallon(s) lemon juice')
print(f'{water3:.2f} gallon(s) water')
print(f'{agave3:.2f} gallon(s) agave nectar')