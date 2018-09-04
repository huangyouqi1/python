#!/usr/bin/env python
#-*- coding: utf-8 -*-
print abs(10)
x=abs(-10)
print x
f=abs
print f(-10)
'''函数名也是变量

那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！'''
'''把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数了！

当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。要恢复abs函数，请重启Python交互环境。

注：由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10。'''


'''传入函数

既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。'''
def add (x,y,f):
	print f(x)+f(y)

add(-5,-6,abs)	
'''我们先看map。map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。'''
def f(x):
	return x*x

print map(f,[1,2,3,4,5,6,7,8,9,10])	
print map(str,[1,2,3,4,5,6,7,8,9,10])	
'''再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：'''

'''reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：'''
def f(x1,x2):
	return x1*x2
print reduce(f,[1,2,3,4,5,6,7,8,9])
'''reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累加计算，其效果就是：'''
def add(x1,x2):
	return x1+x2
print reduce(add,[1,2,3,4,5,6,7,8,9])	
def fn(x,y):
	return 10*x+y
	
print reduce(fn,[1,2,3,4,5])	
def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]#切片

print reduce(fn,map(char2num,'12345'))

def str2int(s):
	def fn(x,y):
		return x*10+y
		
	def char2num(s):	
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]#切片

	return reduce(fn,map(char2num,s))
	
print str2int('12345')	
def char2num(s):	
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]#切片
def str2int(s):
	return reduce(lambda x,y:10*x+y,map(char2num,s))
print str2int('123456789')	
print '012345'[3]


'''和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

例如，在一个list中，删掉偶数，只保留奇数，可以这么写：'''
def is_odd(n):
	return n%2==0
print filter(is_odd,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

def not_empty(s):
	return s and s.strip()
print filter(not_empty,['A','','B',None,'C',' '])	


'''排序算法

排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1，这样，排序算法就不用关心具体的比较过程，而是根据比较结果直接排序。

Python内置的sorted()函数就可以对list进行排序：'''
print sorted([23,26,20,12,25,38])
'''此外，sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。比如，如果要倒序排序，我们就可以自定义一个reversed_cmp函数：'''
def reversed_cmp(x,y):
	if x>y:
		return -1
	if x<y:
		return 1
	return 0	
print sorted([23,26,20,12,25,38],reversed_cmp)






'''可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。'''

print sorted(['bob','about','Zoo','Credit'])
'''默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能定义出忽略大小写的比较算法就可以：'''

def cmp_ignore_case(s1,s2):
	u1=s1.upper()
	u2=s2.upper()
	if u1>u2:
		return 1
	if u1<u2:
		return -1
	return 0
	
print sorted(['bob','about','Zoo','Credit'],cmp_ignore_case)
'''函数作为返回值

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。'''
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum	
	
f=lazy_sum(1,2,3,4,5)	
print f()
f1=lazy_sum(1,2,3,4,5)	
f2=lazy_sum(1,2,3,4,5,6)	
print f1()
print f2()

'''在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：'''

'''
闭包

注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。

另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：'''
def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3=count()
print f1()
print f2()
print f3()

'''全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：'''
def count():
	fs=[]
	for i in range(1,4):
		def f(j):
			def g():
				return j*j
			return g
		fs.append(f(i))
	return fs
f1,f2,f3=count()
print f1()
print f2()
print f3()	

'''当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：'''

print map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])
'''通过对比可以看出，匿名函数lambda x: x * x实际上就是：'''
def f(x):
	return x*x
'''关键字lambda表示匿名函数，冒号前面的x表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：'''
	
f=lambda x:x*x
print f(5)
def build(x,y):
	return lambda x,y:x*x+y*y
l=build(1,2)		
print l(1,2)

'''由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。'''
def new():
	print '2018-08-01'
f=new
print f()	
print new.__name__
print f.__name__

'''现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：'''
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call %s():' %func.__name__
		return func(*args,**kw)
	return wrapper

'''观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：'''
@log
def now_time():
	print '2018-08-01 23:57:59'
	
print now_time()	
'''由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：'''
import functools
def log(text):
	def decorataor(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print '%s %s():'%(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorataor
	
@log('execute')
def now():
	print '2018-08-01'

print now()	
'''now = log('execute')(now)'''	
print now.__name__	

'''因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：'''
'''
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw)
		print 'call %s():' % func.__name__
		return func(*args,**kw)
	return wrapper
	
'''
'''在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：

int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：'''
print int('12345')
print int('12345',base=8)
print int('12345',base=16)
'''假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：'''
def int2(x,base=2):
	return int(x,base)
print int2('1000')	
'''functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：'''
import functools
int2=functools.partial(int,base=2)
print int2('1000')	
'''所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。'''

max2=functools.partial(max,10)
print max2(5,6,7)



























