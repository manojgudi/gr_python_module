import gras
import numpy

class dsim(gras.Block):

	def __init__(self):
		gras.Block.__init__(self,
			name="dsim",
			in_sig=[numpy.float32],
			out_sig=[numpy.float32])	

	def set_parameters(self,a,b,c,d,e,f):
		self.param1 = a #n0
		self.param2 = b #n1
		self.param3 = c #st
		self.param4 = d #d0
		self.param5 = e #d1
		self.n = f #window

	def work(self, input_items, output_items):
		
		#self.n = min(len(input_items[0]), len(output_items[0]))
		in0 = input_items[0]
		out = output_items[0]
		
		from dsim_sci import discrete_sim
		#Processing 
		# Assuming n = 1 input_config(0)=1
		
		out[:self.n] = discrete_sim(self.param1, self.param2, self.param3, self.param4,
					self.param5,in0[:self.n])
		print out[:self.n], in0[:self.n]
		
		self.produce(0,self.n) # Produce from port 0 output_items
		self.consume(0,self.n) # Consume from port 0 input_items
