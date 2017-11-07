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
#可变参数
def calc(*numbers): #第一种调用方式，可变参数不确定
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print("平方和为",calc(1,2))
nums = (1,2)  #第二种调用方式，可变参数已经给出，也可直接调用
print(calc(*nums))
#关键字参数
def person(name,age,**kw):
    return('name:',name,'age:',age)
print(person('yangyinna',24,))