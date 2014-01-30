from __future__ import division # For operations with floating numbers
import time
import serial

# Initialize Serial port, default {baud 9600, stop_bits 1 {1.5, 2}, byte_size 8{5..8}
def ser_init(baud, bytesize, parity, stopbits):
	'''Returns a Serial object instance'''
	# Automatic port detection
	ports=['USB2', 'USB1', 'USB0', 'S0']
	
	for val in ports:
		try:
			port='/dev/tty'+val
			print port
			ser = serial.Serial(port, baud,  bytesize, parity,  stopbits)
			print("serial found on" + val)
			break
		except:
			ser = -1
			print "Couldn't Open Serial Port /dev/tty" + val + " Failed"
			pass
	
	return(ser) 

#ser_init(9600, 8, 'N', 1)

def ser_read(delay=1, count=1, baud=9600, bytesize=serial.EIGHTBITS, parity='N', stopbits=serial.STOPBITS_ONE):
	
	'''ser_read(delay, count, baud, bytesize, parity, stopbits) where delay represents time delay after which serial value will be fetched, minimum/default value is 1 second, count is maximum number of serial values to be fetched, by default it is 1, default {baud 9600, stop_bits 1 {1.5, 2}, byte_size 8{5..8}
	'''

	# Call ser_init()
	ser = ser_init(baud, bytesize, parity, stopbits)
	
	if (ser) == -1 : 
		print "Serial port couldn't be initialized"
	else:
		# Open the port
		ser.open()
		
		# Return array of Serial value
		data=[]

		for i in range(count):
			ser.flushInput()
			data.append(ser.readline())

			# Formatting Output
			temp = data[i]
			temp = float(temp[:temp.find('\n')])
			data[i] = temp

			time.sleep(delay)

		return data	

print(ser_read(.5,7))

