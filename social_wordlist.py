from itertools import combinations, permutations


author = "Shaun"

val = input("How many words: ")
keyword = [0]*int(val)
special = [0]*6
special[0] = "!"
special[1] = "@"
special[2] = "#"
special[3] = "$"
special[4] = "%"
special[5] = "&"


for i in range(0,len(special)):
	print(special[i])

value = int(val)

for x in range(0, value):
	keyword[x] = input("Value: ")

#FUNCTIONS
def first(f):
	
	i = 0
	while(i<value - 1):
		
		#NORMAL
		#f.write(keyword[0]+'\n')
		#f.write(keyword[0][::-1]+'\n')
		f.write(keyword[0] + keyword[i+1]+ '\n')
		f.write(keyword[0] + "_" + keyword[i+1]+ '\n')
		
		for k in range(1, len(keyword) + 1):
			#Frist + other with underscore
			f.write(keyword[0] + keyword[i+1] + "_" + keyword[value-k-i] + '\n')
			f.write(keyword[0] + "_" + keyword[i+1] + keyword[value-k-i]+ '\n')
			#First + others
			f.write(keyword[0] + keyword[i+1] + keyword[value-k-i]+ '\n')
		
		#LAST REVERSED
		f.write(keyword[0] + keyword[i+1][::-1]+ '\n')
		f.write(keyword[0] + "_" + keyword[i+1][::-1]+ '\n')	
		
		for k in range(1, len(keyword) + 1):		
			#Underscore first
			f.write(keyword[0] + "_" + keyword[i+1][::-1] + keyword[value-k-i]+ '\n')
			f.write(keyword[0] + "_" + keyword[i+1] + keyword[value-k-i][::-1]+ '\n')
			f.write(keyword[0] + "_" + keyword[i+1][::-1] + keyword[value-k-i][::-1]+ '\n')
			#Underscore second
			f.write(keyword[0] + keyword[i+1][::-1] + "_" + keyword[value-k-i]+ '\n')
			f.write(keyword[0] + keyword[i+1] + "_" + keyword[value-k-i][::-1]+ '\n')
			f.write(keyword[0] + keyword[i+1][::-1] + "_" + keyword[value-k-i][::-1]+ '\n')
		
		#FIRST REVERSED
		f.write(keyword[0][::-1] + keyword[i+1]+ '\n')
		f.write(keyword[0][::-1] + "_" + keyword[i+1]+ '\n')
		
		for k in range(1, len(keyword) + 1):
			f.write(keyword[0][::-1] + "_" + keyword[i+1] + keyword[value-k-i]+ '\n')
			f.write(keyword[0][::-1] + keyword[i+1] + "_" + keyword[value-k-i]+ '\n')
		i+=1
		
		
def last(f):
	k = value - 1
	while(k>0):
	
		#NORMAL
		#f.write(keyword[value-1]+'\n')
		#f.write(keyword[value-1][::-1]+'\n')
		f.write(keyword[value-1] + keyword[k-1]+ '\n')
		f.write(keyword[value-1] + "_" + keyword[k-1]+ '\n')
		
		for l in range(0, len(keyword)):
			#Frist + other with underscore
			f.write(keyword[value-1] + keyword[k-1] + "_" + keyword[0 + l]+ '\n')
			f.write(keyword[value-1] + "_" + keyword[k-1] + keyword[0 + l]+ '\n')
			#First + others
			f.write(keyword[value-1] + keyword[k-1] + keyword[0 + l]+ '\n')
		
		#FIRST REVERSED
		f.write(keyword[value-1][::-1] + keyword[k-1]+ '\n')
		f.write(keyword[value-1][::-1] + "_" + keyword[k-1]+ '\n')
		
		for l in range(0, len(keyword)):
			f.write(keyword[value-1][::-1] + keyword[k-1] + "_" + keyword[0+l]+ '\n')
			f.write(keyword[value-1][::-1] + "_" + keyword[k-1] + keyword[0+l]+ '\n')
			
		#LAST REVERSED
		f.write(keyword[value-1] + keyword[k-1][::-1]+ '\n')
		f.write(keyword[value-1] + "_" + keyword[k-1][::-1]+ '\n')
		
		for l in range(0, len(keyword)):
			#Underscore first
			f.write(keyword[value-1] + "_" + keyword[k-1][::-1] + keyword[0+l]+ '\n')
			f.write(keyword[value-1] + "_" + keyword[k-1] + keyword[0+l][::-1]+ '\n')
			f.write(keyword[value-1] + "_" + keyword[k-1][::-1] + keyword[0+l][::-1]+ '\n')
			#Underscore second
			f.write(keyword[value-1] + keyword[k-1][::-1] + "_" + keyword[0+l]+ '\n')
			f.write(keyword[value-1] + keyword[k-1] + "_" + keyword[0+l][::-1]+ '\n')
			f.write(keyword[value-1] + keyword[k-1][::-1] + "_" + keyword[0+l][::-1]+ '\n')
			
		k-=1


def iteratively(f):
	i = 0
	while(i < value-1):
		#NORMAL
		f.write(keyword[i]+'\n')
		f.write(keyword[i][::-1]+'\n')
		f.write(keyword[i] + keyword[i+1]+ '\n')
		f.write(keyword[i] + "_" + keyword[i+1]+ '\n')
			
		for k in range(1, len(keyword) + 1):
			#Underscore first
			f.write(keyword[i] + "_" + keyword[i+1] + keyword[value-k-i]+ '\n')
			#Underscore second
			f.write(keyword[i] + keyword[i+1] + "_" + keyword[value-k-i]+ '\n')
			#The "i" index + others
			f.write(keyword[i] + keyword[i+1] + keyword[value-k-i]+ '\n')
		
		#FIRST REVERSED
		f.write(keyword[i][::-1] + keyword[i+1]+ '\n')
		f.write(keyword[i][::-1] + "_" + keyword[i+1]+ '\n')
		
		for k in range(1, len(keyword) + 1):
			f.write(keyword[i][::-1] + "_" + keyword[i+1] + keyword[value-k-i]+ '\n')
			f.write(keyword[i][::-1] + keyword[i+1] + "_" + keyword[value-k-i]+ '\n')
			
		#LAST REVERSED
		f.write(keyword[i] + keyword[i+1][::-1]+ '\n')
		f.write(keyword[i] + "_" + keyword[i+1][::-1]+ '\n')	
		
		for k in range(1, len(keyword) + 1):
			#Underscore first
			f.write(keyword[i] + "_" + keyword[i+1][::-1] + keyword[value-k-i]+ '\n')
			f.write(keyword[i] + "_" + keyword[i+1] + keyword[value-k-i][::-1]+ '\n')
			f.write(keyword[i] + "_" + keyword[i+1][::-1] + keyword[value-k-i][::-1]+ '\n')
			#Underscore second
			f.write(keyword[i] + keyword[i+1][::-1] + "_" + keyword[value-k-i]+ '\n')
			f.write(keyword[i] + keyword[i+1] + "_" + keyword[value-k-i][::-1]+ '\n')
			f.write(keyword[i] + keyword[i+1][::-1] + "_" + keyword[value-k-i][::-1]+ '\n')
		
		i+=1
		
		
	k = value - 1
	while(k > 0):
		#NORMAL
		f.write(keyword[k]+'\n')
		f.write(keyword[k][::-1]+'\n')
		f.write(keyword[k] + keyword[k-1]+ '\n')
		f.write(keyword[k] + "_" + keyword[k-1]+ '\n')
		
		for l in range(0, len(keyword)):
			#Underscore first
			f.write(keyword[k] + "_" + keyword[k-1] + keyword[0 + l]+ '\n')
			#Underscore second
			f.write(keyword[k] + keyword[k-1] + "_" + keyword[0 + l]+ '\n')
			#The "k" index + others
			f.write(keyword[k] + keyword[k-1] + keyword[0 + l]+ '\n')
		
		#FIRST REVERSED
		f.write(keyword[k][::-1] + keyword[k-1]+ '\n')
		f.write(keyword[k][::-1] + "_" + keyword[k-1]+ '\n')
		
		for l in range(0, len(keyword)):
			f.write(keyword[k][::-1] + keyword[k-1] + "_" + keyword[0+l]+ '\n')
			f.write(keyword[k][::-1] + "_" + keyword[k-1] + keyword[0+l]+ '\n')
			
		#LAST REVERSED
		for l in range(0, len(keyword)):
			#Underscore first
			f.write(keyword[k] + "_" + keyword[k-1][::-1] + keyword[0+l]+ '\n')
			f.write(keyword[k] + "_" + keyword[k-1] + keyword[0+l][::-1]+ '\n')
			f.write(keyword[k] + "_" + keyword[k-1][::-1] + keyword[0+l][::-1]+ '\n')
			#Underscore second
			f.write(keyword[k] + keyword[k-1][::-1] + "_" + keyword[0+l]+ '\n')
			f.write(keyword[k] + keyword[k-1] + "_" + keyword[0+l][::-1]+ '\n')
			f.write(keyword[k] + keyword[k-1][::-1] + "_" + keyword[0+l][::-1]+ '\n')	
			
		k-=1


def all_reverse(f):
	i = 0
	while(i<value - 1):
		f.write(keyword[0][::-1] + keyword[i+1][::-1] + '\n')
		f.write(keyword[0][::-1] + "_" + keyword[i+1][::-1] + '\n')
		
		
		
		for k in range(1, len(keyword) + 1):
			#First + rest
			f.write(keyword[0][::-1] + keyword[i+1][::-1] + keyword[value-k-i][::-1]+ '\n')
			#Underscore first
			f.write(keyword[0][::-1] + "_" + keyword[i+1][::-1] + keyword[value-k-i][::-1]+ '\n')
			f.write(keyword[0][::-1] + "_" + keyword[i+1][::-1] + keyword[value-k-i][::-1]+ '\n')
			f.write(keyword[0][::-1] + "_" + keyword[i+1][::-1] + keyword[value-k-i][::-1]+ '\n')
			#Underscore second
			f.write(keyword[0][::-1] + keyword[i+1][::-1] + "_" + keyword[value-k-i][::-1]+ '\n')
			f.write(keyword[0][::-1] + keyword[i+1][::-1] + "_" + keyword[value-k-i][::-1]+ '\n')
			f.write(keyword[0][::-1] + keyword[i+1][::-1] + "_" + keyword[value-k-i][::-1]+ '\n')
			
		i+=1
		
	k = value - 1
	while(k>0):
		f.write(keyword[value-1][::-1] + keyword[k-1][::-1] + '\n')
		f.write(keyword[value-1][::-1] + "_" + keyword[k-1][::-1] + '\n')
		
		for l in range(0, len(keyword)):
			#First + rest
			f.write(keyword[value-1][::-1] + keyword[k-1][::-1] + keyword[0+l][::-1]+ '\n')
			#Underscore first
			f.write(keyword[value-1][::-1] + "_" + keyword[k-1][::-1] + keyword[0+l][::-1]+ '\n')
			f.write(keyword[value-1][::-1] + "_" + keyword[k-1][::-1] + keyword[0+l][::-1]+ '\n')
			f.write(keyword[value-1][::-1] + "_" + keyword[k-1][::-1] + keyword[0+l][::-1]+ '\n')
			#Underscore second
			f.write(keyword[value-1][::-1] + keyword[k-1][::-1] + "_" + keyword[0+l][::-1]+ '\n')
			f.write(keyword[value-1][::-1] + keyword[k-1][::-1] + "_" + keyword[0+l][::-1]+ '\n')
			f.write(keyword[value-1][::-1] + keyword[k-1][::-1] + "_" + keyword[0+l][::-1]+ '\n')
		k-=1

#first()
#last()
#iteratively()
#all_reverse()

with open('wordlist.txt', 'w') as f:
	first(f)
	last(f)
	iteratively(f)
	all_reverse(f)
