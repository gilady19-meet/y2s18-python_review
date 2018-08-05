# Write your solution for 1.1 here!
a=0
import random
for i in range(100):
	if i%2==0:
		 a=a+i
print(a)
z=0
x=0
y=0
for x in range(1000):
	if x%6==2:
		if (x*x*x)%5 ==3:
			y=x

print(y)
s=0
f=1
m=0
while s<10000:
	f=f+1
	if f%2==0:
		s=s+f
		m=m+1
print(m)

def is_prime(x):
	pass
	n=0
	for i in range(2, x/2+1):
		if x%i==0:
			n+=1
	if n==0:
		return "true"
	else:
		return "false"

print(is_prime(5191))

class superheroe(object):
	def __init__(self, name , superpower , strength):
		self.name = name
		self.superpower=superpower
		self.strength=strength
	def details(self):
		return(self.name + str(self.strength))
	def save_civilian(self, work):
		self.strength = self.strength - work
		if self.strength>=0:
			return self.strength
		else:
			return("the super hero is not strong enough")



superman=superheroe("superman" , "fly" , 100)
print(superman.details())
print(superman.save_civilian(700))

print(random.randint(1,10))

while 1<9:
	print("Gilad Yosef is a King")