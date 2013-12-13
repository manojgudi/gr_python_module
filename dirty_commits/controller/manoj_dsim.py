import gras
import numpy
from daq import *

class dsim(gras.Block):

	def __init__(self):
		gras.Block.__init__(self,
			name="dsim",
			in_sig=[numpy.float32],
			out_sig=[numpy.float32])	
		self.q1 = Queue(3)
		#self.q2 = Queue(3)
		#self.q3 = Queue(3)	

		self.t_1 = 0
	def set_parameters(self,p,i,d,a,b,f):
		self.proportional = p 
		self.integtime = i
		self.derivtime = d
		self.delt = a #del_t
		self.setpt = b #set_point
		#self.param6 = c #st
		#self.param7 = d1 #d0
		#self.param8 = e #d1
		self.n = f #window
	
	def work(self, input_items, output_items):
		
		#n = min(len(input_items[0]), len(output_items[0]))
		in0 = input_items[0][0]
		out = output_items[0]
		
		self.err1 = in0 - self.setpt
		
		print 't-1',self.t_1
		self.q1.push(self.t_1)
		self.q1.push(self.err1) # Should this be in0?
		
		'''
		self.q2.push(in0)
		
		#self.q2.pop()
		self.q3.push(in0)
		self.q3.push(in0)
		self.q3.pop()		
		'''
		
		self.t_0 = in0
		self.t_1 = self.q1.pop()
		self.t_2 = self.q1.pop()
		#from dsim_sci import csim
		#Processing 
		# Assuming n = 1 input_config(0)=1
		
		out[:1] = (self.proportional * (self.err1 - self.t_1)
                	+(self.delt/self.integtime)*self.err1+ 
			(self.derivtime/self.delt)*(self.err1 - 2*self.t_1
			+self.t_2 ))
		
		#print out, in0
		print 's',self.setpt
		print 'in',in0
		print 'Err',self.err1
			
	
		output_items[0] = output_items[0].tolist()
		output_items[0].append(out)

		#print output_items[0]
		self.consume(0,1) # Consume from port 0 input_items
		self.consume(1,1)
		#parser.add_argument("-d1",help="coefficient of numerator")
		#parser.add_argument("-d2",help="coefficient of numerator")
		self.produce(0,1) # Produce from port 0 output_items
