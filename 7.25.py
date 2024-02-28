def exact_change(user_total):
    num_dollars = 0
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0
    while user_total != 0:
        if user_total >= 100:
            num_dollars += 1
            user_total = user_total - 100
        elif user_total >= 25:
            num_quarters += 1
            user_total = user_total - 25
        elif user_total >= 10:
            num_dimes += 1
            user_total = user_total - 10
        elif user_total >= 5:
            num_nickels += 1
            user_total = user_total - 5
        elif user_total >= 1:
            num_pennies += 1
            user_total = user_total - 1
    if user_total == 0:
        if num_dollars == 1:
            print("1 dollar")
        elif num_dollars > 1:
            print(f'{num_dollars} dollars')
        if num_quarters == 1:
            print("1 quarter")
        elif num_quarters > 1:
            print(f'{num_quarters} quarters')
        if num_dimes == 1:
            print("1 dime")
        elif num_dimes > 1:
            print(f'{num_dimes} dimes')
        if num_nickels == 1:
            print('1 nickel')
        elif num_nickels > 1:
            print(f'{num_nickels} nickels')
        if num_pennies == 1:
            print('1 penny')
        elif num_pennies > 1:
            print(f'{num_pennies} pennies')
        if num_dollars == 0 and num_quarters == 0 and num_dimes == 0 and num_nickels == 0 and num_pennies == 0:
            print('no change')
input_val = int(input())
num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
