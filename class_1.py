#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student object (name:%s)' % self.name
	__repr__=__str__	
#print Student('Michael')	
s=Student('hyq')

print s	

class Fib(object):
	def __init__(self):
		self.a,self.b=0,1
	def __iter__(self):
		return self
	def next(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>100000:
			raise StopIteration()
		return self.a	
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b=1,1
			for x in range(n):
				a,b=b,a+b
			return a
		if isinstance(n,slice):
			start=n.start
			stop=n.stop
			a,b=1,1
			L=[]
			for x in range(stop):
				if x>=start:
					L.append(a)
				a,b=b,a+b	
			return L	
for n in Fib():
	print n
f=Fib()
print f[5]	
print f[5:10]

class Student(object):
	def __init__(self):
		self.name='Michael'
	def __getattr__(self,attr):
		if attr=='score':
			return 99
		if attr=='age':
			return lambda:25
		raise AttributeError('\'Student\' object has no attribute\'%s\''%attr)	
	def __call__(self):
		print ('My name is %s '% self.name)
s=Student()
print s.name		
print s.score	
print s.age
s()





def fn(self,name='world'):
	print('Hello,%s' % name)
	
Hello=type('Hello',(object,),dict(hello=fn))
h=Hello()
h.hello()
print(type(Hello))
print(type(h))
	