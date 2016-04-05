import numpy as numpi
def createGraph(filename):
	myMap = {}
	count = 0
	prev = ""
	with open(filename, 'r') as myfile:
		data = myfile.read().splitlines()
		for j in data:
			if(count%2 == 1):
				myMap[prev] = j.split()
			count+=1
			prev = j
		return myMap
def deleteCopies(array):
	temp = []
	for j in array:
		if(j not in temp):
			temp.append(j)
	return temp
def getNeighbors(users, curr, prev):
	nbrs = []
	if(curr in users.keys()):
		nbrs+=users[curr]
	for coach in users.keys():
		if(curr in users[coach]):
			nbrs+=users[coach]
			nbrs.append(coach)
	return nbrs
def findUser(target, users):
	for a in users:
		if (target in a):
			return True
	return False
def infection(users, start):
	if(not start):
		return "Please enter a valid input"
	if(start not in users.keys() and not findUser(start, users.values())):
		return start+" is not in the system"
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
	return "Users that recieve new features: "+ str(deleteCopies(final))
temp = createGraph(raw_input('Enter a file name: '))
infected = infection(temp, raw_input('Enter start of spread: '))
print
print(str(numpi.sort(numpi.array(infected)).tolist()))
print