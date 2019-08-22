#C:\Users\Mike\AppData\Local\Programs\Python\Python37-32\python.exe C:\Users\Mike\Desktop\python\collatzProcessExplorer.py

#(ax+c)/2 if odd
#(bx+d)/2 if even

#of a and c, one should be 1 and one should be 3
a = 3
b = 1
# c is odd
c = 1
#d is even
d = 0

n = 0

x = n

trajectory = []
	
seenBefore = 0

numbersSeen = []

while n < 30:
	
	i = 0
	
	while i < len(numbersSeen):
		
		if x == numbersSeen[i]:
		
			seenBefore = 1
			
			break
			
		i += 1
				
	if seenBefore == 1:
	
		if len(trajectory) > 0:
		
			y = trajectory[-1]
			
			if y%2 == 1:
				y = int((a*y + c)/2)
			
			elif y%2 == 0:
				y = int((b*y + d)/2)
		
			trajectory.append(y)
		
			print(trajectory)
	
		n += 1
		
		x = n
		
		trajectory = []
	
		seenBefore = 0
		
	else:
	
		numbersSeen.append(x)
	
		trajectory.append(x)
	
		if x%2 == 1:
			x = int((a*x + c)/2)
			
		elif x%2 == 0:
			x = int((b*x + d)/2)