#！/usr/bin/python3

a,b = 10,20

list = [1,2,3,4,5];  # 列表

if (a in list):
    print('变量 a 在给定的列表中 list 中')
else:
    print('变量 a 不在给定的列表中 list 中')

if (b not in list):
    print('变量 b 不在给定的列表中 list 中')
else:
    print('变量 b 在给定的列表中 list 中')


a = 3
if (a in list):
    print('变量 a 在给定的列表中 list 中','a等于：',a)
else:
    print('变量 a 不在给定的列表中 list 中')


a,b= 20,20
if(a is b):
    print('a 和 b 有相同的标识')
else:
    print('a 和 b 没有相同的标识')
a=19
if(a is not b):
    print('a 和 b mei有相同的标识')
else:
    print('a 和 b 有相同的标识!')