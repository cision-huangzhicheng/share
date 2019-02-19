#！/usr/bin/python3

x = True
y = False
z = False

if  not x or not y:
    print(1)
else:
    print(0)
if not x or  y or not y and  z:
    print(2)
elif not x or y or not y and x:
    print(3)

if x and y:
    print(99)
else:
    print(100)