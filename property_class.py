#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
class Student(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value<0 or value>100:
			raise ValueError('score must between 0~100')
		self._score=value	
	@property	
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,value):
		self._birth=value
	@property
	def age(self):
		return 2018-self._birth

		
s=Student()
s.score=100 #实际转化为s.set_score(100)
print s.score	#实际转化为s.get_score()
s.birth=1993	
print 'age=%d' % s.age	

class Animal(object):
	pass
#大类
class Mammal(Animal):
	pass
class Bird(Animal):
	pass
#各种动物
class Dog(Mammal):
	pass
class Bat(Mammal):
	pass
class Parrot(Bird):
	pass
class Osrich(Bird):
	pass
	
class RunnableMixIn(object):
	def run(self):
		print('Running...')
class FlyableMixIn(object):
	def fly(self):
		print('Flying...')
class Dog(Mammal,RunnableMixIn):
	pass
	'''
class Student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student object (name:%s)' %self.name		
	def __repr__(self):
		return 'show:%s' %self.name 
print Student('hyq')		
s=Student('12346')
s