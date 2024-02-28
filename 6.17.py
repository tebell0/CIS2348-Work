a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
check = False
for x in range(-10, 11, 1):
    for y in range(-10, 11, 1):
        if a * x + b * y == c and d * x + e * y == f:
            check = True
            print(x, y)
if check == False:
    print("No solution")