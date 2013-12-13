# Data Acquisition list based queue

class Queue: 
    """A sample implementation of a First-In-First-Out
       data structure."""
    def __init__(self, length):
        self.in_stack = [] 
        self.out_stack = []
	self.length = length
 
    def push(self, obj):
        if len(self.in_stack) < self.length:
		self.in_stack.append(obj)
	else:
		print "Queue Full"

    def pop(self):
    	try:
        	if not self.out_stack:
	            	while self.in_stack:
				self.out_stack.append(self.in_stack.pop())
		return self.out_stack.pop()
	except:
		print "Queue empty"

    def size(self):
   	return len(self.out_stack)
