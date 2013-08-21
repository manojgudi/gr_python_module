#!/usr/bin/python -tt


def calc_op(n0,n1,n2,  d0,d1,d2):
	string1 = "s=%s; h=syslin('c',"
	string2 = str(n0)+"*s^2+"+str(n1)+"*s+"+str(n2)+","
	string3 = str(d0)+"*s^2+"+str(d1)+"*s+"+str(d2)+");"
	string4 = "t=0:0.01:10;"
	string5 = "deff('u=input(t)','u=abs(sin(t))');"
	string6 = "r=tf2ss(h); a=csim(input,t,r);"

	full_string = string1+string2+string3+string4+string5+string6
	
	print "ex:"

	print full_string

	import sciscipy
	sciscipy.eval(full_string)
	b = sciscipy.read("a")
	t = sciscipy.read("t")
	print "output is ",b
	return b


print calc_op(1,2,4, 2,3,1)
