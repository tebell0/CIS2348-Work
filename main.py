password = input()
if 'i' in password:
    password = password.replace('i', '!')
if 'a' in password:
    password = password.replace('a', '@')
if 'm' in password:
    password = password.replace('m', 'M')
if 'B' in password:
    password = password.replace('B', '8')
if 'o' in password:
    password = password.replace('o', '.')
add = 'q*s'
newpass = password + add
print(newpass)
