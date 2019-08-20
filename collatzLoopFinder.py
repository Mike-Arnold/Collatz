#C:\Users\Mike\AppData\Local\Programs\Python\Python37-32\python.exe C:\Users\Mike\Desktop\python\collatzLoopFinder.py

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

	
#c here refers to the one in ax + c
cMin=1  #the starting value, so it should be odd
cMax=2	#should at least cMin+1

loops = [] 
indexOfC = 0  #as we check each c, we'll place each new loop in loops[indexOfC] 
loopCounter = 0  #this will be equivalent to len(loops[indexOfC])-1, but for readability we'll always just add +1 manually

currentC = cMin
loops.append([currentC])  #label the first row of loops

while currentC < cMax:
	trajectorySeed = 0
	#print(currentC)
	
	while trajectorySeed < 2000:  #loops tend to contain small values, so checking up to a relatively large number should capture all of them
	
		trajectoryPoint = trajectorySeed  #trajectoryPoint is the x in 3x+1
		trajectory = [trajectoryPoint] #the complete history of where trajectoryPoint gets sent by this process
		loopFound = 0
		
		while loopFound == 0:
			
			#iterate on trajectoryPoint
			if trajectoryPoint%2 == 0:  		#if is even
				trajectoryPoint = int(((1*trajectoryPoint) + 0) / 2)		#can change the zero on this line to be any even number
																
			elif trajectoryPoint%2 == 1:				#if x is odd
				trajectoryPoint = int(((3*trajectoryPoint) + currentC) / 2)
				
			#append the new trajectoryPoint to trajectoryPoint's history
			trajectory.append(trajectoryPoint)
			
			possibleMatchIndex = 0 #we'll use trajectory[possibleMatchIndex] to check if the newest trajectoryPoint has occured before
			
			while possibleMatchIndex < len(trajectory)-1:
										#we check up to the length of trajectoryPoint's history, minus one to ignore its current point
										
				#if trajectoryPoint matches an earlier point trajectory[possibleMatchIndex], we may have a new loop
				if trajectory[possibleMatchIndex] == trajectoryPoint:
					#this will let us exit this starting number n
					loopFound = 1
					
					#first, cycle tempTraj so its lowest point is first
					
						#some new variables for this purpose
					tempTraj = trajectory[possibleMatchIndex:len(trajectory)-1]  #take a clip of trajectory at the two points that matched
					tempTrajIterator=1   #the value at this index will be compared to the current lowest to see which is lower
					lowestPointIndex = 0 #bookmarks the current champion, will be used to cut the tempTraj in half
					
						#find the index of the lowest point in the trajectory
					while tempTrajIterator < len(tempTraj):										#go through the whole clip tempTraj,
					
						if abs(tempTraj[tempTrajIterator]) < abs(tempTraj[lowestPointIndex]):	#check if any element is lower than the current champ,
							lowestPointIndex = tempTrajIterator									#if it is, make it the new champ.
							
						tempTrajIterator += 1
					
					loop = tempTraj[lowestPointIndex:]+tempTraj[:lowestPointIndex]	#cut tempTraj in half at the lowest point and put the rear part in front
					
						#then, check if it already appears
					loopChecker = 0
					
					while loopChecker <= loopCounter:
					
						if loopChecker == loopCounter:
							#we've checked everything up to the number of loops, no match, so it's new
							print(str(len(loop))+" "+str(loop))
							loops[indexOfC].append(loop)
							loopCounter += 1
							break
						
						elif loop == loops[indexOfC][loopChecker+1]:  #we add the one because the first element is "c"
							#old loop, break
							break
						
						loopChecker += 1
					
					#because we matched an earlier value, we're done looking
					break
					
				else:
					possibleMatchIndex += 1
					
		
		#the following 3 if statements shuffle the seed to its next starting point
		if trajectorySeed == 0:
			trajectorySeed = 1
		elif trajectorySeed > 0:
			trajectorySeed = -trajectorySeed
		else:
			trajectorySeed = -trajectorySeed + 2 #add 2 because we only need to check odd starting values, other than zero
	
	#print(loops[indexOfC])
	print(str(loopCounter) + " loops for " + str(currentC))
	print("")
	currentC += 2
	indexOfC += 1
	loops.append([currentC])  #attach a label of 'C' to a new row of loops
	loopCounter = 0