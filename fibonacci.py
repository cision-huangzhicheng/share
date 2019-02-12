#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib (n):
    a,b = 0,1
    while b < n:
        print(b,end=' ')
        a,b = b,a+b
    print()

#def fib2(n):
#    result = []
#    a,b = 0,1
#    while b < n:
#        result.append(b)
#        a,b = b,a+b
#    return result
def fib2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

fib(1000)


fib2(100)