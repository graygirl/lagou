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