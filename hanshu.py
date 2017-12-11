# -*- coding:utf-8 -*-
'''
#调用函数
#print(abs(-100))
#print(abs(-100,2))  #给出的参数不符合规定会报错
print(int('123'))
print(int(123.32))

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
    print('name:',name,'age:',age,'other:',kw)
print(person('yangyinna',24,city = 'shanghai'))
#命名关键字参数
def person(name,age,*,job = 'engineer',city): #命名关键字函数可以有缺省值
    print(name,age,job,city)
print(person('yangyinna',24,job = 'engineer',city = 'shanghai'))
#参数组合 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a,b,c = 10,*args,**kw):
    print('a: ',a,'b: ',b,'c: ',c,'args = ',args,'kw = ',kw)
print(f1(1, 2, 3, 'a', 'b', x=99))
args = (1, 2, 3, 4) #*args是可变参数，args接收的是一个tuple
kw = {'d': 99, 'x': '#'} #**kw是关键字参数，kw接收的是一个dict
print(f1(*args,**kw))
#递归函数
def jiecheng(n):
    if n == 1:
        return 1
    return n * jiecheng(n-1)
print(jiecheng(10))
#尾递归函数
def jiecheng(n):
    return jiecheng_iter(n,1)
def jiecheng_iter(num,product):
    if num == 1:
        return product
    return jiecheng_iter(num - 1,num * product)
print(jiecheng_iter(10,1))

#切片
l = list(range(100))
print(l[2:6])
#迭代
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k,v in d.items():
    print(k,v)
#判断一个对象是否为可迭代对象
from collections import Iterable
print(isinstance('abx',Iterable))
#把一个list变成索引-元素对
for i,v in enumerate(['a','b','c']):
    print(i,v)

#列表生成式
print(list(range(1,11)))
L = []
for x in range(1,11):
    L.append(x * x)
print(L)

print([x * x for x in range(1,5) if x % 2 == 0])
#os.listdir可以列出文件和目录
import os
print([d for d in os.listdir('.')])

#生成器，可以用next调用
g = (x * x for x in range(10))
print(next(g))
for n in g:
    print(n)

#斐波那契额函数
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b #将print(b)改为yield b则变成生成器，遇到yield函数将会返回，再次执行时将上次返回的语句继续执行
        a,b=b,a+b
        n=n+1
    return 'done'
f=fib(5)
while True:
    try:
        x=next(f)
        print('f:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
'''
#函数式编程
#传入函数
def add(x,y,abs):
    return(abs(x)+abs(y))
print(add(5,-12,abs))
