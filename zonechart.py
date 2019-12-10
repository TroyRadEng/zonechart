#python sketch for the internal workings of chore assignment

import array as arr
import random

rotation = -1

#here's the list of what the chores will be called
chores = []

#1st element is zone name, 2nd name is zone urgency, 3rd name is zone urgency delta
chores.append(["Downstairs Lounge + Front Room Cleaning", 0, 1])	 #zone 0
chores.append(["Upstairs Kitchen & Front Room", 0, 1])			 #zone 1
chores.append(["Upstairs Bathroom", 0, 0.75])			 	 #zone 2
chores.append(["Downstairs Bathroom", 0, 0.75])			 	 #zone 3
chores.append(["Front Stairs", 0, 0.5])					 #zone 4
chores.append(["Back Stairs", 0, 0.5])					 #zone 5
chores.append(["Basement Organizing", 0, 0.25])				 #zone 6
chores.append(["Backyard", 0, 0.5])					 #zone 7
chores.append(["Attic", 0, 0.25])					 #zone 8
chores.append(["Middle Room", 0, 0.25])					 #zone 9
chores.append(["Mowing/Shoveling/Raking", 0, 0.5])			 #zone 10
chores.append(["Downstairs Lounge + Front Room Organizing", 0, 0.25])    #zone 11
chores.append(["Upstairs Lounge + Front Room Organizing", 0, 0.25])	 #zone 12

#1st element is person's name, 2nd element is their assigned zone, 3rd element is the list of chores they do not do
people = []
people.append(["Oliver",5,[1,2,12]])
people.append(["Mark",4,[1,2,12]])
people.append(["Mike",3,[0,3,11]])
people.append(["Katie",2,[0,3,11]])
people.append(["Merv",1,[0,3,8,11]])
people.append(["Dylan",0,[0,3,11]])

while True:
	rotation += 1
	print("Rotation "+str(rotation+1))
	print("=======================================")

	#increment and print chore urgency

	print("Zone Urgency:")
	for i in range(0, len(chores)):
		chores[i][1] += chores[i][2]
		print("* "+chores[i][0]+": "+str(chores[i][1]))
	print("=======================================")

	#assign people to appropriate chores

	rand = random.randint(1,len(people))-1
	for i in range(0, len(people)):
		i_rand = (i + rand)%len(people) #this is so that tasks are assigned in random order (for more fair variation in assignments)
		for j in range(0, len(chores)):

			#check whether the current task is on a person's "do not do" list

			donotassign = 0
			for x in range (0, len(people[i_rand][2])):
				if people[i_rand][2][x] == j:
					donotassign = 14
			if (donotassign == 0) and (chores[j][1] > chores[people[i_rand][1]][1]): #i.e if the urgency of the given chore is higher than the urgency of whatever the person is assigned to now
				people[i_rand][1]=j
		chores[people[i_rand][1]][1] = 0
		print(people[i_rand][0]+" is assigned to "+chores[people[i_rand][1]][0])
	print("=======================================")


	input("Press Enter to continue...")
	print(" ")
	print(" ")
	print(" ")
	print(" ")
	print(" ")