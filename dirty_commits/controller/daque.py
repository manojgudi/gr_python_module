class Queue:	
	def __init__(self,length):	
		self.in_stack=[1]*length
		self.out_stack=[1]*length

	def push(self,obj):
		self.in_stack.append(obj)
	def pop(self):
		if not self.out_stack:
			while self.in_stack:
				self.out_stack.append(self.in_stack.pop())
		return self.out_stack.pop()
		
