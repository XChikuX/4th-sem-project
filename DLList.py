class DLList:

	class node:
		def __init__(self):
			self.element = None
			self.next = None
			self.prev = None


	def __init__(self):
		self.head =self.node()
		self.tail = self.head
		self.sz = 0


	def returnLast(self):
		return

	def insertLast(self,u):
		if (self.head.element == None):
			self.head.element = u.element
			self.sz+=1
		else:
			# Cheack this too
			self.tail.next = u
			u.prev = self.tail
			self.tail = u
			self.tail.next=self.head
			self.head.prev=self.tail
			self.sz+=1
		return

	def insertFirst(self,u):
		if (self.head.element == None):
			self.head.element = u.element
			self.head.next=self.head
			self.head.prev=self.head
			self.tail=self.head
			self.sz+=1
		else:
			#SOMETHING WORNG HERe
			u.next = self.head
			u.prev=self.tail
			self.head.prev=u
			self.head = u
			self.tail.next=self.head
			self.sz+=1
		return


	def deleteFirst(self):
		return

	def insertAfter(self,u,v):
		return

	def insertBefore(self,u,v):
		return

	def deleteNode(self,val):
		curnode=self.findNode(val)
		curnode.prev.next=curnode.next
		curnode.next.prev=curnode.prev
		del curnode

	def findNode(self, val):
		curnode = self.head
		lastnode = self.tail
		while curnode!=lastnode:
			if curnode.element.player_name == val:
				return curnode
			elif lastnode.element.player_name == val:
				return lastnode
			curnode = curnode.next
			lastnode = lastnode.prev
		if (curnode.element.player_name == val):
			return curnode
		return None
		
	def printList(self):
		tnode = self.head
		print tnode.element
		tnode = tnode.next
		while tnode!= self.head:
			print tnode.element
			tnode = tnode.next
		return

	def isEmpty(self):
		return 

	def size(self):
		return self.sz
