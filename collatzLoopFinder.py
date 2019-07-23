#C:\Users\Mike\AppData\Local\Programs\Python\Python37-32\python.exe C:\Users\Mike\Desktop\python\collatz.py

#The Collatz Conjecture or 3x+1 problem concerns a process of taking a starting number, x, and either
#multiplying it by 3 and adding one (if x is odd), 
#or dividing it by 2 (if x is even).
#The process repeats indefinitely.  
#Depending on the starting number x, this can either get stuck in a loop, or continue without ever repeating.
#The conjecture states that every positive number will eventually reach 1 (or 1,4,2,1,4,2,1 etc).

#For example, 28 has 28,14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1.
#So 28 required 18 steps, while 26 required 10.
#Meanwhile, 27 can also be checked, and it requires 111 steps.
#There is no general formula for the number of steps required.

#If negative numbers are included, we also find 3 negative loops.
#There is also a loop at 0. (0,0,0,0...)


#The classic problem involves 3x+1, however we may also look at the behavior of 3x+c more generally.
#Each different c added after multiplying by 3 will give different loops.
#If a loop exists for 3x+c, a similar set of loops will exist for 3x+3c.
#But in general, it is not possible to predict what new loops will exist.
#Evidently, at least one new loop will always be found when multiplying c by a factor other than 3.

#This script finds loops for a given range of c.

#First, we start a given x on its trajectory.
#On each iteration we check if the new x has appeared before.
#When a repeat is found, we copy down the possible loop.
	#The loop is cycled so the lowest element is first
#Then we check our loop candidate against the current list of loops.
#If it does not match any previous loop, it is added to the list of loops.

#Then we either flip to the negative case of c, or flip back to the positive case and add two.
	#c must be odd.

cMin=1
cMax=10
indexOfC = 0
loopCounter=0
loops = [[c]]

c = cMin
while c < cMax:
	n=0
	#print(c)
	
	while n < 2000:
	
		x=n
		trajectory=[x] #the complete history of where x gets sent by this process
		loopFound=0
		
		while loopFound == 0:
			
			#iterate on x
			if x%2 == 0:  				#if x is even
				x = int(((1*x) + 0) / 2)
				
			elif x%2 == 1:				#if x is odd
				x = int(((3*x) + c) / 2)
				
			#append the new x to x's history
			trajectory.append(x)
			
			y=0 #we'll use traj[y] to check if the newest x has occured before
			z=len(trajectory)-1 #we check up to the length of x's trajectory
								#we exclude traj[-1] because that's x itself
			
			while y < z:
			
				#if we match an earlier number in the trajectory, we may have a new loop
				if trajectory[y] == x:
					#this will let us exit this starting number n
					loopFound = 1
					
					#first, cycle traj[y:z] so its lowest element is first
					w=1
					traj = trajectory[y:z]
					least = traj[0]
					leastIndex = 0
					
					while w < len(traj):
						if abs(traj[w]) < abs(least):
							least = traj[w]
							leastIndex = w
						w += 1
					
					loop = traj[leastIndex:]+traj[:leastIndex]
					
					#then, check if it already appears
					v=0
					
					while v <= loopCounter:
					
						if v == loopCounter:
							#we have a new loop
							print(str(len(loop))+" "+str(loop))
							loops[indexOfC].append(loop)
							loopCounter +=1
							v = loopCounter+1
						
						elif loop == loops[indexOfC][v+1]:
							#old loop, move v to end
							v = loopCounter+1
						
						v += 1
					
					#because we matched an earlier value, we're done looking
					y=z
					
				else:
					y += 1
					
		if n == 0:
			n = 1
		elif n > 0:
			n = -n
		else:
			n = -n + 2 #add 2 because we only need to check odd starting values, other than zero
	
	#print(loops[indexOfC])
	print(str(loopCounter) + " loops for " + str(c))
	print("")
	c += 2
	indexOfC += 1
	loops.append([c])
	loopCounter = 0