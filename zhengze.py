#!/usr/bin/env python
#-*- coding: utf-8 -*-
import re
if re.match(r'^\d{3}\-\d{3,8}$','010-12345'):
	print 'ok'
else:
	print 'failed'
if re.match(r'^\d{3}[\s\-]+\d{3,8}$','010-12345'):
	print 'ok'
else:
	print 'failed'	
print re.split(r'\s+','a b  c')	
print re.split(r'[\s\,]+','a,b,  c  d')	
print re.split(r'[\s\,\;]+','a,b, c ;; d')	
m=re.match(r'^(\d{3})[\s\-]+(\d{3,8})$','010 - 12345678')
print m.group(0)
print m.group(1)
print m.group(2)
