#!/usr/bin/python

import sciscipy


# u is a TUPLE vector of width w

def discrete_sim(n0,n1,st,d0,d1,u):
        code_string1 = "s=%s;"
        code_string2 = "h=syslin("
        code_string3 = str(st)+","+str(n0)+"*s"+"+"+str(n1)+","+str(d0)+"*s"+"+"+str(d1)+");"
        code_string4 = "r=tf2ss(h);"
        code_string5 = "u="+str(list(u))+";"
        code_string6 = "y=dsimul(r,u)"
        code_string = code_string1 + code_string2 + code_string3 + code_string4 + code_string5 + code_string6

	# Check complete_code_string 
	#print code_string

	import sciscipy
	sciscipy.eval(code_string)
	y = sciscipy.read("y")
	return y

#print discrete_sim(1,1,0.1,2,1,"u=zeros(1,50);u(10)=1")

if __name__ == "__main__":
	u = [0]*100
	u[50:100] = [1]*50
	out = discrete_sim(1,1,0.1,2,1,u)
	import matplotlib.pyplot as plt
	plt.plot(out)
	plt.show()
