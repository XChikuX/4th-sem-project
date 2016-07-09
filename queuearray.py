from random import *
class MyQueue():
	def __init__(self):
		self.queue = []
		# Moved front and rear to -1
		self.f = -1
		self.r = -1
		self.max_queue_size =6
		for i in range(0,self.max_queue_size):
			self.queue.append(None)
			
	def enqueue(self,value):
		#print (self.f, ":", self.r)
		if (self.size() == self.max_queue_size):
			print("Overflow")
		elif self.f == self.r and self.f == -1:
			self.r+=1
			self.f+=1
			self.queue[self.r]=value
		else:
			self.r+=1
			self.r = (self.r)%(self.max_queue_size)
			self.queue[self.r] = value	
				
	def dequeue(self):
		#print (self.f, ":", self.r)
		if (self.size()==0):
			return "Queue Empty Exception"
		elif (self.f==self.r):
			obj = self.queue[self.f]                
			self.queue[self.f] = None
			self.f=self.r=-1
			return obj
		else:
			obj = self.queue[self.f]                
			self.queue[self.f] = None
			self.f = (self.f+1)%(self.max_queue_size)
			return obj
            
	def rotate(self):
		x=  randint(0,20)
		y= randint(20,40)
		print (x," :: ",y)
		for i in range(x,y):
			a=self.dequeue()
		
			self.enqueue(a)
			
			
	def load_revolver(self):
		self.enqueue("Bullet")
		for i in range(5):
			self.enqueue("Empty")
 
	def front(self):
		if (self.isEmpty()==0):
			print ("returning front element")
			return self.queue[self.f]
		else:
			return "Queue Empty Exception"
	
	def isEmpty(self):
		if (self.f == -1):
			#print ("Queue empty")
			return True
		else:
			#print ("Queue not empty")
			return False
        

	def size(self):
		if self.isEmpty()==False:
			return (self.max_queue_size - self.f + self.r )%(self.max_queue_size)+1
		else:
			return 0
