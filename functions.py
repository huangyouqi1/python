#!/usr/bin/env python
#-*- coding: utf-8 -*-

print abs(-123)
'''比较函数cmp(x, y)就需要两个参数，如果x<y，返回-1，如果x==y，返回0，如果x>y，返回1：'''
print cmp(1,2)
print cmp(2,1)
print cmp(2,2)
#数据类型转换
print int('123')
print int(12.3)
print float('12.3')
print str(12.3)
print unicode(123)
print bool(1)
print bool('')


'''在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。'''
#判断函数参数x的数据类型是否对，异常处理用raise
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else :
		return -x
def my_cmp(x,y):
	if x>y:
		return 1
	elif x<y:
		return -1
	else :
		return 0	
print my_abs(1)
print my_abs(-1)
print my_cmp(1,2)
print my_cmp(2,1)
print my_cmp(2,2)		

def nop():
	pass

#pass 可以起到占位的作用
age=19	
if age>=18:
	pass

#函数可以返回多个值，其实是返回一个tuple的元组，也可以用多个变量来接收函数的返回值，即元组
def scan(x):
	nx=1
	ny=2
	nz=3
	return nx,ny,nz
	

r=scan(1)
print r	

#函数参数，除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
print power(5,3)
'''从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。'''

def enroll(name,gender,age=6,city='shenzhen'):
	print 'name:',name
	print 'gender:',gender
	print 'age:',age
	print 'city:',city


enroll('hyq','F')	
#也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。
enroll('hyq','M',city='Beijing')

#可变参数，仅仅在参数前面加一个*号
def calc(numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum
	
print calc([1,2,3])#传一个列表
print calc((1,2,3))#传一个元组

def calc_1(*numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum
	
print calc_1(1,2,3)	#参数加一个*就变成了可变参数，随便传各种参数	
#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
num=[1,2,3]
print calc_1(*num)

#关键参数
'''可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。'''
def person(name,age,**kw):
	print 'name:',name,'age:',age,'other:',kw
person('hyq',25)	
person('Adam',45,gender='M',job='Engineer')
#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
kw={'city':'Beijing','job':'Engineer'}
person('Hyq',25,**kw)
'''参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。'''

def func(a,b,c=0,*args,**kw):
	print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw
func(1,2)
func(1,2,c=3)
func(1,2,3,'a','b')	
func(1,2,3,'a','b',x=99)	
#最神奇的是通过一个tuple和dict，你也可以调用该函数
args=(1,2,3,4)
kw={'x':99}
func(*args,**kw)

#递归函数
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)	

print fact(100)	
'''递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：'''
'''解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：'''
def fact(n):
	return fact_iter(n,1)

def fact_iter(num,product):
	if num==1:
		return product
	return fact_iter(num-1,num*product)	
print fact(5)	
































	
	