import queue as q
import numpy as np
import copy

def neighbors(state): #function to find children of a given state
	index = np.asarray(np.where(state == 0)).T
	x = index[0][0]
	y = index[0][1]
	neighborStates = []
	if y-1 >= 0:
		upState = copy.deepcopy(state)
		upState[x][y], upState[x][y-1] = upState[x][y-1], upState[x][y]
		neighborStates.append(upState)
	if x-1 >= 0:
		leftState = copy.deepcopy(state)
		leftState[x][y], leftState[x-1][y] = leftState[x-1][y], leftState[x][y]
		neighborStates.append(leftState)
	if y+1 < 5:
		downState = copy.deepcopy(state)
		downState[x][y], downState[x][y+1] = downState[x][y+1], downState[x][y]
		neighborStates.append(downState)
	if x+1 < 5:
		right = [x+1, y]
		rightState = copy.deepcopy(state)
		rightState[x][y], rightState[x+1][y] = rightState[x+1][y], rightState[x][y]
		neighborStates.append(rightState)
	return neighborStates

def h1(state, goal): #function for the misplaced tiles heuristic
	misplaced = 0
	for i in range(5):
		for j in range(5):
			if state[i][j]!=goal[i][j]:
				misplaced+=1
	return misplaced

def array_in(arr, arr_list): #function to determine if a given state (arr) appears in the closed list (arr_list)
	for elem in arr_list:
		if(arr == elem).all():
			return True
	return False

if __name__ == '__main__':
	#initialize the starting and goal states
	goalState = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15],[16, 17, 18, 19, 20],[21, 22, 23, 24, 0]])
	initialState = np.array([[3, 17, 9, 5, 21],[11, 0, 13, 19, 10],[6, 24, 22, 1, 20],[16, 14, 4, 12, 15],[18, 8, 23, 2, 7]])
	#goalState = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 0]])
	#initialState = np.array([[0, 2, 8],[1, 5, 4],[7, 3, 6]])
	#declare a priority queue, closed list, and counter variable for the informed search
	open = q.PriorityQueue()
	closed = []
	#counter used as a tie-breaker for the situation when more than 1 state in the fringe has the same heuristic value (priority)
	counter = 0
	#determine the initial state's heuristic value
	priority = h1(initialState, goalState)
	#initialize the open list with the starting state
	open.put((priority, counter, initialState))
	#while the fringe is not empty
	while open:
		#get the next state to check
		current = open.get()
		print(current)
		#exit condition
		if np.array_equiv(current[2], goalState):
			break
			print("solution found")
			closed.append(current[2])
			print(closed)
		else:
			#get children of the current node
			neighborStates = neighbors(current[2])
			#for each child of the current node
			for state in neighborStates:
				#check that the child has not been visited
				if not array_in(state, closed):
					#if not visited, increment counter
					counter += 1
					#add child to closed list
					closed.append(state)
					#find the heuristic value and add to open list, continue looping
					priority = h1(state, goalState)
					open.put((priority, counter, state))
