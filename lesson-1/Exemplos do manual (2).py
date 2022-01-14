#------------------------------------------------------------------------------
import os as s
import math as m
import time as t
import calendar as c
#from math import *
#from math import sqrt
#------------------------------------------------------------------------------
s.system("Color 7D")
a = (18.0)
print("-"*45)
print ("A raiz quadrada de %1.f é" %(a), m.sqrt(a))
print ("-"*45)

#print ("A raiz quadrada de %1.f é" %(a), sqrt(a))

#print ("A raiz quadrada de %1.f é" %(a), sqrt(a))

#------------------------------------------------------------------------------
local2 = t.localtime(t.time())
print("Local current time:",local2)
print("-"*45)
local = t.asctime(t.localtime(t.time()))
print("Horario local:", local)
print("-"*45)

#-------------------------------------------------------------------------------
calen = c.month(2016, 12)
print("",calen)
print("-"*80)

calenda = c.calendar(2016)
print("",calenda)
print("-"*80)
t.sleep(30)


