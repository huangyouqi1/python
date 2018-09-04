#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Student(object):
	pass

s=Student()
s.name=	'huangyouqi' #动态给实例绑定一个属性
print s.name
def set_age(self,age):
	self.age=age
	
from types import MethodType
s.set_age=MethodType(set_age,s)#给实例绑定一个方法，这个方法对其它实例不起作用
s.set_age(25)
print s.age	


s2=Student()
#print s2.age

def set_score(self,score):
	self.score=score
	
Student.set_score=set_score	#给类绑定一个方法之后，对所有的实例都有效
s.set_score(100)
print s.score
s2.set_score(90)
print s2.score
'''使用__slots__
但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
'''
class Student(object):
	__slots__=('name','age')#用tuple元组定义运行绑定的属性名称
s=Student()
s.name='hyq'
s.age=25
#s.score=99#score属性已被限制	
print s.name
print s.age

'''使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：'''
class GraduateStudent(Student):
	pass

g=GraduateStudent()
g.score=9999
print g.score	
