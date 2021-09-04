#Are they the same?

a = [121, 144, 19, 161, 19, 144, 19, 11,0]

b = [121, 14641, 20736, 361, 25921, 361, 20736, 361,3]

a.sort()

b.sort()

flag = True

x = 0

for i in b:
    if i != a[x]*a[x]: 
        flag = False
    x += 1

if flag:
    print("True")
else:
    print("False")
