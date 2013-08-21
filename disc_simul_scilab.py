#!/usr/bin/python

import sciscipy
sciscipy.eval("s=%s;h=syslin(0.5,s+1,s+5);r=tf2ss(h);u=zeros(1,50);u(10)=1;y=dsimul(r,u);a=size(y)//;disp(a)")
y=sciscipy.read("y")
a=sciscipy.read("a")
print y
print a
