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
