import gras
import numpy

class square3_ff(gras.Block):

	def __init__(self):
		gras.Block.__init__(self,
			name="square3_ff",
			in_sig=[numpy.float32],
			out_sig=[numpy.float32])


	def work(self, input_items, output_items):
		
		#n = min(len(input_items[0]), len(output_items[0]))
		n=1
		in0 = input_items[0]
		out = output_items[0]
		
		from disc_simul_scilab import discrete_sim
		#Processing 
		# Assuming n = 1 input_config(0)=1
		
		out[:n] = discrete_sim(2,3,0.5,1,2,str(in0[:n][0]))
		
		print out[:n], in0[:n]

		self.consume(0,n) # Consume from port 0 input_items
		self.consume(1,n) # Consume from port 1 input_items
		self.produce(0,n) # Produce from port 0 output_items
