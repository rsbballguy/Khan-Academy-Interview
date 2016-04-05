import numpy as numpi
def createDataStructures(filename): #creates two data structures, a map with coach as key and list of users as values, and another that is a list of all users
	myMap = {}
	users = []
	count = 0
	prev = ""
	with open(filename, 'r') as myfile:
		data = myfile.read().splitlines()
		for j in data:
			if(count%2 == 1):
				myMap[prev] = j.split()
				if(prev not in users):
					users.append(prev)
				for a in myMap[prev]:
					if(a not in users):
						users.append(a)
			count+=1
			prev = j
		return (myMap, users)
def deleteCopies(array): #helper method to delete copies in list/array
	temp = []
	for j in array:
		if(j not in temp):
			temp.append(j)
	return temp
def getNeighbors(users, curr, prev): #gets neighbors of any user
	nbrs = []
	if(curr in users.keys()):
		nbrs+=users[curr]
	for coach in users.keys():
		if(curr in users[coach]):
			nbrs+=users[coach]
			nbrs.append(coach)
	return nbrs
def infection(users, start): #spreads "infection" through all connected coaches and students
	visited = []
	final = []
	curr = []
	curr.append(start)
	final.append(start)
	while(1):
		temp = []
		for j in curr:
			if(j not in visited):
				temp += getNeighbors(users, j, final)
				visited.append(j)
		curr = temp
		final+=curr
		if(not curr):
			break
	return deleteCopies(final)
def limited(map, users, target): #Prints best possible scenario given the target number requested
	graphs = []
	visitedusers = []
	for user in users:
		if (user not in visitedusers):
			curr = numpi.sort(numpi.array(infection(map, user))).tolist()
			graphs.append(curr)
			visitedusers+=curr
	graphs = sorted(graphs,key = len)
	prev = []
	if(int(target) <= 0):
		print "No user recieved the new features"
		return ("None", "")
	for graph in graphs:
		if(len(graph) == int(target)):
			return (graph, "It is exactly the target number requested")
		else:
			if(len(prev) < int(target) and len(graph) > int(target)):
				return (prev, "Its "+str(int(target) - len(prev))+ " less than the target number")
			elif(len(prev) > target):
				return (prev, "It is "+str(len(prev) - int(target))+ " more than the target number") 
		prev = graph
	return (graphs[len(graphs)-1], "It is "+str(int(target)-len(graphs[len(graphs)-1])) + " less than the target number")
temp = createDataStructures(raw_input('Enter a file name: '))
final = limited(temp[0], temp[1], raw_input('Enter target number of people to spread feature to: '))
print("Users that recieve new features: " + str(final[0]))
print(final[1])