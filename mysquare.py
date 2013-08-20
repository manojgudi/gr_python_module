import gras
import numpy

class square3_ff(gras.Block):
	

	def __init__(self):
		gras.Block.__init(self,
			name="square3_ff"
			in_sig=[numpy.float32],
			out_sig=[numpy.float32])

	def work(self, input_items, output_items):
		in0 = input_items[0]
		out = output_items[0]

		out[:] = in0 * in0

		return len(output_items[0])
