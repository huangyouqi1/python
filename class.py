#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def  print_score(self):
		print '%s:%s' % (self.name,self.score)
	def get_grade(self):
		if self.score >=90:
			print 'A'
		elif self.score>=60:
			print 'B'
		else:
			print 'C'
		

bart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)
bart.print_score()
bart.get_grade()
lisa.print_score()	
lisa.get_grade()
class Man(object):
	def __init__(self,height,weight):
		self._height=height
		self._weight=weight
	def get_height(self):	
		print self._height
	def get_weight(self):
		print self._weight
	def set_height(self,height):
		if 100<height<200:
			self._height=height
		else:
			raise ValueError('height error')
	def set_weight(self,weight):
		if 30<weight<100:
			self._weight=weight
		else:
			raise ValueError('weight error')	
			
man=Man(170,50)		
man.set_height(185)
man.set_weight(60)

man.get_height()
man.get_weight()

class Animal(object):
	def run(self):
		print 'Animal is runing...'

class Dog(Animal):
	def run(self):
		print 'Dog is runing...'
	def eat(self):
		print 'Eating meat...'
class Cat(Animal):
	def run(self):
		print 'Cat is runing...'
		
dog=Dog()
cat=Cat()
dog.run()
dog.eat()	
cat.run()	

'''子类可以看作是是父类，因为子类继承了父类的所有属性，但父累不一定是子类Dog可以看成Animal，但Animal不可以看成Dog。'''
def run_twice(animal):
	animal.run()
	animal.run()
run_twice(Animal())	
run_twice(Dog())	
run_twice(Cat())	
class Tortoise(Animal):
	def run(self):
		print 'Tortoise is runing slowly...'

run_twice(Tortoise())	

print type(123)	
print type('str')	
print type(None)	
print type(abs)	
import types
def fn():
	pass
	
print type(fn)==types.FunctionType	
print type(abs)==types.BuiltinFunctionType
print type(lambda x:x)==types.LambdaType
print type((x for x in range(10)))==types.GeneratorType

class Husky(Dog):
	pass
	
a=Animal()
d=Dog()
h=Husky()
print isinstance(h,Husky)
print isinstance(h,Dog)
print isinstance(h,Animal)	
print isinstance([1,2,3],(list,tuple))
print isinstance((1,2,3),(list,tuple))

#print dir('ABC') 
import PIL.Image
#print dir(PIL.Image)

class MyObject(object):
	def __init__(self):
		self.x=9
	def power(self):
		print self.x*self.x

obj=MyObject()
print hasattr(obj,'x')
print hasattr(obj,'y')
setattr(obj,'y',19)
print hasattr(obj,'y')
print getattr(obj,'y')
print obj.y
#print getattr(obj,'z')
print getattr(obj,'z',404)

print hasattr(obj,'power')
print getattr(obj,'power')
fn=getattr(obj,'power')
fn()









		