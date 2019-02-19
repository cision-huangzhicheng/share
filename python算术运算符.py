#！/usr/bin/python3

a,b,c = 21,10,0

c = a + b
print("1 .c的值为： ", c)
c = a % b   #去模- 返回一个除法大的余数
print("2. c的值为：",c)

#修改变量a ,b ,c
a,b = 2,3
c = a ** b # **就是2 的3次方
print("6. c 的变量为：",c)

#//向下去整除数的整数
a,b = 11,5
c = a // b
print("7. c的值为",c)