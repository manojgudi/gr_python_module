import gras
import numpy

class square3_ff(gras.Block):

	def __init__(self):
		gras.Block.__init__(self,
			name="square3_ff",
			in_sig=[numpy.float32],
			out_sig=[numpy.float32])


	def work(self, input_items, output_items):
		
		n = min(len(input_items[0]), len(output_items[0]))
		in0 = input_items[0]
		out = output_items[0]
		
		out[:n] = in0[:n] * in0[:n]

		self.consume(0,n)
		self.produce(0,n)
