#!/usr/bin/env python
#-*- coding: utf-8 -*-
l=[]
n=1
while n<99:
	l.append(n)
	n+=2
print l	
print range(1,99,2)
L=['Michael','Sarah','Tracy','Bob','Jack']
r=[]
n=3
for i in range(n):
	r.append(L[i])
print r	

'''对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作'''

print L[0:3]
print L[:3]
print L[1:3]
print L[-2:]

L=range(100)
print L[80:90]
print L[:90:3]
#所有数，每5个取一个：
print L[::5]
print L[-20:]
'''tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：'''
print (0,1,2,3,4,5,6,7,8,9)[:3]
'''字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：'''
print 'ABCDEFGHIJKLNMOPQRSYZW'[0:6]

'''如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。'''
d={'a':1,'b':2,'c':3}
for key in d:
	print key

for value in d.itervalues():
	print value
for k,v in d.iteritems():
	print k ,v
for ch in 'ABC':
	print ch
	
#判断是否可以迭代
from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance(123,Iterable)	
'''最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：'''
for i,value in enumerate(['A','B','C']):
	print i,value
for x,y in[(1,1),(2,3),(3,9)]:
	print x,y
'''列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。'''

L=[]
for x in range(1,11):
	L.append(x*x)
print L	

print [x*x for x in range(1,11)]
print [x*x for x in range(1,11) if x%2==0]
print [m+n for m in 'ABC' for n in 'XYZ']

import os
print [d for d in os.listdir('.')]
d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
	print k,'=',v
	
print [k+'='+v for k,v in d.items()]	

L=['Hello','World',18,'Apple',None]
print [s.lower() for s in L if isinstance(s,str)]

'''通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：'''

L=[x*x for x in range(10)]
print L
G=(x*x for x in range(10))
print G.next()
print G.next()
print G.next()
print G.next()

for n in G:
	print n
'''
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print b
		a,b=b,a+b
		n+=1
fib(4)	
'''	
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n+=1	
for n in fib(6):		
	print n
'''这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。'''		
		