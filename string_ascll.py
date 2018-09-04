#!/usr/bin/env python
#-*- coding: utf-8 -*-
print ord('A')
print chr(65)
print u'中文'
#print u'中文'.encode('utf-8')
print u'ABC'.encode('utf-8')
print len(u'ABC')
print len(u'中文')
print u'中文测试正常'
print 'Hi,%s,you have $%d' %('huangyouqi',1000000)
print 'growth rate :%d%%' % 99