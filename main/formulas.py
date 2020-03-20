from __future__ import division
import math
def triangular(x,a,b,c):
	print ("triangular   " + str(max( min( ((x-a)/(b-a)),((c-x)/(c-b))),0)))
	#print(res)
#	print min((x-a)/(b-a) , (c-x)/(x-b))
#	print (x-a)
#	print (b-a)
#	print ((x-a) / (b-a))
#	print (c-x/x-b)
#	print (c-x)
#	print (x-b)
def trapezoidal(x,a,b,c,d):
	res=max( min( (x-a)/(b-a), 1,(d-x)/(d-c) ),0)
	print( "trapezoidal "+str(res))

def gaussian(x,b,c):
	print ("gaussian   " +str( math.exp ( (-1/2) *  (  ( (x-c) /b )  ) ** 2)))

def generalized(x,b,c):
	print (" generalized   " + str(1  /  (1 + ( ( (x-c)  / b) **2) )))
	#print (x-c)
	#print (x-c /b )
def generalizedB(x,b,c):
         print  ("generalizedB    "+     str(1 / ( 1 + abs((x-c)/b)**2*b)))


#def menu():
#	while(i != 0)
#		i=input("que ")
#		triangular(4,2,3,4)
#		switch (i):
#			case 1:

triangular(160,0,120,190)
trapezoidal(2,0,1,9,20)
generalized(24,5,15)
generalizedB(24,5,15)
gaussian(24,5,15)