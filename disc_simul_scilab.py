#!/usr/bin/python

import sciscipy
import matplotlib.pyplot as plt

def discrete_sim(n0,n1,st,d0,d1,u):
        string1 = "s=%s;"
        string2 = "h=syslin("
        string3 = str(st)+","+str(n0)+"*s"+"+"+str(n1)+","+str(d0)+"*s"+"+"+str(d1)+");"
        string4 = "r=tf2ss(h);"
        string5 = "u="+str(u)+";"
	string5 = u+";"
        string6 = "y=dsimul(r,u)"
        string = string1+string2+string3+string4+string5+string6

	# Check complete_string 
	#print string

	import sciscipy
	sciscipy.eval(string)
	y = sciscipy.read("y")
	plt.plot(y)
	plt.show()
	return y

print discrete_sim(1,1,0.1,2,1,"u=zeros(1,50);u(10)=1")

