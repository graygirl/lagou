# -*- coding:utf-8 -*-
'''
#调用函数
#print(abs(-100))
#print(abs(-100,2))  #给出的参数不符合规定会报错
print(int('123'))
print(int(123.32))
'''
#定义函数
def myabs(x):
    if x > 0:
        return(x)
    else:
        return(-x)
print(myabs(-5))
#空函数
def nop():
    pass
#位置参数
def power(x,n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s
print('x: %s 的 n: %s 次方为: '%(5,2),power(5,2))
#默认参数
def power1(x,n=2):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s
print('x: %s 的 n: %s 次方为: '%(5,3),power1(5,3))
