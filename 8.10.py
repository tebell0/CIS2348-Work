string = input().strip('')
string2 = string.replace(" ", '')
string3 = string2[::-1]
if string3 == string2:
    print(f'{string} is a palindrome')
else:
    print(f'{string} is not a palindrome')