from DLList import *
from queuearray import *
class Player:
	
	def __init__(self):
		self.group=DLList()
		self.player_name=""
		self.player_age=0
		self.kill=[]
		
		
		
	class play:
		def __init__(self):
			self.player_name=raw_input("Enter player name : \n")
			self.player_age=input("Enter player Age : \n")
			self.slot=MyQueue()
	def insertplayer(self):
		data=DLList.node()
		data.element=self.play()
		self.group.insertFirst(data)

		
		
	def deleteplayer(self,name):
		ct=0
		curnode=self.group.head
		if curnode.next!=self.group.head:
			for i in range(self.group.size()):
				if curnode.element.player_name==name:
					ct+=1
					#self.group.deleteNode(self.group.element.player_name)
					curnode.prev.next=curnode.next
					curnode.next.prev=curnode.prev
					del curnode
					print "Deleted curnode and shifted"
					break
				curnode=curnode.next
				print "GOing next"
		else:
			if curnode.element.player_name==name:
				ct+=1
				del curnode
				print "Deleted curnode"
		if ct==0:
			print ("Not found")
			self.group.sz+=1
		self.group.sz-=1
		
	def playerkill(self):
		curnode=self.group.head
		for i in range(player.group.size()):
			curnode=curnode.next
			if self.kill[i]:
				self.deleteplayer(curnode.element.player_name)
		self.kill=[]
						
	def printplayer(self,n):
		tnode=self.group.head
		i=0
		while(i<n):
			tnode=tnode.next
			i+=1
		print "Name : ",tnode.element.player_name,"  "
		print "Age: ",tnode.element.player_age

	def playerready(self):
		#print "Getting ready"
		curnode=self.group.head
		x= self.group.size()
		for i in range(x):
			
			curnode.element.slot.load_revolver()
			curnode=curnode.next
		#self.group.slot.load_revolver()
			curnode.element.slot.rotate()
		print "Players are ready to shoot"
		
	def playershoot(self):
		curnode=self.group.head
		x= self.group.size()
		for i in range(x):
			
			if curnode.element.slot.dequeue()=="Bullet":
				self.kill.append(1)
			else:
				self.kill.append(0)	
			print self.kill
			curnode=curnode.next
		#print "Shoot ready"
		
			
	
player=Player()
x=input("Enter number of players")
for i in range(x):
	player.insertplayer()

player.group.printList()
ch='y'
while ch=='y' or ch=='Y':
	while player.group.size()>1:
		player.playerready()
		player.playershoot()
		for i in range(player.group.size()):
			player.printplayer(i)
		'''for i in range(player.group.size()):
		if player.kill[i]:
			deleteplayer()
		'''
		player.playerkill()
		for i in range(player.group.size()):
			player.printplayer(i)
	
	print "Continue?? : Y/N"
	if player.group.size()<2:
		break	
	ch=raw_input()

