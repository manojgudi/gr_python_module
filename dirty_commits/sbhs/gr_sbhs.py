import gras
import numpy
import serial
import time
from sbhs import *
from scan_machines import *

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
ser.open()

class gr_sbhs(gras.Block):

	def __init__(self):
		gras.Block.__init__(self,
			name="gr_sbhs",
			in_sig=[numpy.float32, numpy.float32],
			out_sig=[numpy.float32])	
		
		# SBHS init
		self.new_device = Sbhs()
		self.new_device.connect(1)
		self.new_device.connect_device(0)


	def set_parameters(self,window):
		self.n = window
	
	# Check if value of window is integral of length of input source vector 
	# For cases like -> input = [3 , 4, 5 ,6] & window = 3
	def isIntegralWin(self, input_item, window):
		if (len(input_item) % window ):
			raise Exception("Value of Window should be an integral value of length of input items")
			
		
	def work(self, input_items, output_items):
		
		if len(input_items[0]) != len(input_items[1]):
			raise Exception("Heat value vector and Fan Speed Value vector should be of equal length")
			

		# Assuming input_items[0] and input_items[1] have same LENGTH
		for heat_items, fan_items in zip(input_items[0], input_items[1]):
			#Setting Heat
			self.new_device.setHeat(heat_items)
			time.sleep(0.5)
			self.new_device.setFan(fan_items)
			time.sleep(1)


		# Get temperature
		output_items[0] =  self.new_device.getTemp()

		print output_items[0]

		#Write a for loop for n_inputs
		for i in range(len(input_items)):
			self.consume(i,1) # Consume from port 0 input_items

		self.produce(0,self.n) # Produce from port 0 output_items

	def __del__(self):
		ser.close()
		print "destructor"
