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

def h2(state, goal): #sum of distances function (Manhattan heuristic)
	distance = 0
	for i in range(25):
		stateIndex = np.asarray(np.where(state == i)).T #find position of each element in both state and goal and break into x,y components for manipulation
		goalIndex = np.asarray(np.where(goal == i)).T

		stateX = stateIndex[0][0]
		stateY = stateIndex[0][1]
		goalX = goalIndex[0][0]
		goalY = goalIndex[0][1]
		
		distance += (abs(goalX - stateX) + abs(goalY - stateY)) #formula for determining the distance of an individual element between the current state and the goal state
	return distance

def array_in(arr, arr_list): #function to check if a given state (arr) appears in the closed list (arr_list)
	for elem in arr_list:
		if(arr == elem).all():
			return True
	return False


if __name__ == '__main__':
	#initialize the initial and goal states
	goalState = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15],[16, 17, 18, 19, 20],[21, 22, 23, 24, 0]])
	initialState = np.array([[3, 17, 9, 5, 21],[11, 0, 13, 19, 10],[6, 24, 22, 1, 20],[16, 14, 4, 12, 15],[18, 8, 23, 2, 7]])
	#goalState = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 0]])
	#initialState = np.array([[1, 8, 4],[7, 3, 2],[5, 6, 0]])
	#create a fringe(priority queue) and a closed list
	open = q.PriorityQueue()
	closed = []
	#create a counter as a tiebreaker if more than 1 state has the same heuristic (priority)
	counter = 0
	#calculate heuristic of initial state and add it to the fringe
	priority = h2(initialState, goalState)
	open.put((priority, counter, initialState))
	#while the fringe is not empty
	while open:
		#get the next node 
		current = open.get()
		print(current)
		#exit condition
		if np.array_equiv(current[2], goalState):
			break
			print("solution found")
			closed.append(current[2])
			print(closed)
		else:
			#get children of the current state
			neighborStates = neighbors(current[2])
			#for each child
			for state in neighborStates:
				#check if child appears in the closed list
				if not array_in(state, closed):
					#if the child has not been visited
					#increment counter
					counter += 1
					#add child to closed list
					closed.append(state)
					#calculate heuristic and add the child to the open list, continue looping
					priority = h2(state, goalState)
					open.put((priority, counter, state))

	
