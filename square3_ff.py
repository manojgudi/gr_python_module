import gras
import numpy

class square3_ff(gras.Block):

	def __init__(self):
		gras.Block.__init__(self,
			name="square3_ff",
			in_sig=[numpy.float32, numpy.float32],
			out_sig=[numpy.float32])


	def work(self, input_items, output_items):
		
		n = min(len(input_items[0]), len(output_items[0]), len(input_items[1]))
		
		in0 = input_items[0]
		in1 = input_items[1]
		out = output_items[0]
		
		#Processing 
		out[:n] = in0[:n] + in1[:n]
		
		out[:n] = O(c1,c2=1,c3=1,in0[:n])

		print " here"
		print out[:n], in1[:n], in0[:n]

		self.consume(0,n) # Consume from port 0 input_items
		self.consume(1,n) # Consume from port 1 input_items
		self.produce(0,n) # Produce from port 0 output_items
