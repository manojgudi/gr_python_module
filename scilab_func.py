
def calc_op(n0,n1,n2,  d0,d1,d2):
	string1 = "s=%s; h=syslin('c',"
	string2 = str(n0)+"*s^2+"+str(n1)+"*s+"+str(n2)+","
	string3 = str(d0)+"*s^2+"+str(d1)+"*s+"+str(d2)+");"
	string4 = "t=0:0.01:10; r=tf2ss(h); a=csim('step',t,r)"

	full_string = string1+string2+string3+string4
	
	print "ex:"

	print full_string

	print "s=%s;h=syslin('c',s+1,s^2+s+1);t=0:0.01:10;r=tf2ss(h),a=csim('step',t,r)"

	import sciscipy
	sciscipy.eval(full_string)
	b = sciscipy.read("a")
	t = sciscipy.read("t")
	print "output is ",b
	return b


print calc_op(1,2,0, 0,3,1)
