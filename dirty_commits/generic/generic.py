import gras
import numpy

class generic(gras.Block):

	def __init__(self):
		gras.Block.__init__(self,
			name="generic",
			in_sig=[numpy.float32],
			out_sig=[numpy.float32])	

	def set_parameters(self,func_name,window):
		self.n = window
		self.func_name = func_name
	
	# Check if value of window is integral of length of input source vector 
	# For cases like -> input = [3 , 4, 5 ,6] & window = 3
	def isIntegralWin(self, input_item, window):
		if (len(input_item) % window ):
			raise Exception("Value of Window should be integral of length of input items")
			
		
	def work(self, input_items, output_items):
		
		from scilab import Scilab
		Sci = Scilab()
		
		# Check number of input_instances
		n_input_items = len(input_items)
		
		# Create Output Instances
		out = output_items[0]
		out_eval_string = 'eval("Sci.'+self.func_name+'('
		
		# Iterate for n_input_items
		for i in range(n_input_items):
			
			# Check window condition
			self.isIntegralWin(input_items[i][:], self.n)

			# If the window is greater than 1,  input_items[i][:self.n] looks like [1   2   3   4   5] which is err for python since it requires comma as delimiters 
			if self.n == 1:
				out_eval_string = out_eval_string + str(input_items[i][:self.n]) + ","
			else:	
				print 'IN',str(input_items[i][:self.n])
				out_eval_string = out_eval_string + (str(input_items[i][:self.n].tolist()))  + ","  # Replace 10spaces with a singe comma
						
		out_eval_string = out_eval_string.rstrip(",") + ')")'
		print "STRING  ",str(out_eval_string)
		output_items[0][:] = eval(out_eval_string)
		
		print "OUT",out
		
		#Write a for loop for n_inputs
		for i in range(n_input_items):
			self.consume(i,self.n) # Consume from port 0 input_items

		self.produce(0,self.n) # Produce from port 0 output_items
	
