#!/usr/bin/env python3

"""
Project 1
Anna Blendermann
"""

import sys
import heapq
import math


class PriorityQueue:
    	def __init__(self):
        	self.elements = []
    
    	def empty(self):
        	return len(self.elements) == 0
    
    	def put(self, item, priority):
        	heapq.heappush(self.elements, (priority, item))
    
    	def get(self):
        	return heapq.heappop(self.elements)[1]


def parse_map(mapfile):
	"""
	Parse the mapfile
    	Returns the map as an appropriate data structure
    	"""
	map = []
	for line in open(mapfile, "r").readlines():
		new_line = list(line[:-1])
		map.append(new_line)
	return map


def heuristic(v1, v2):
	"""
	Heuristic for A* search
	Finds the euclidean distance between two grid points
	"""
	return math.sqrt((v2[0]-v1[0])**2 + (v2[1]-v1[1])**2)


def heuristic2(v1, v2):
	"""
	Heuristic for A* search
	Finds the manhattan distance between two grid points
	"""
	return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])


def neighbors(grid, v):
	row = v[0]
	col = v[1]
	neighbors = []
	if (row > 0):
		if (grid[row-1][col] != 'w'):
			neighbors.append((row-1, col))
	if (row < len(grid)):
		if (grid[row+1][col] != 'w'):
			neighbors.append((row+1, col))
	if (col > 0):
		if (grid[row][col-1] != 'w'):
			neighbors.append((row, col-1))
	if (col < len(grid[0])):
		if (grid[row][col+1] != 'w'):
			neighbors.append((row, col+1))
	return neighbors


def get_cost(grid, v1, v2):
	row = v2[0]
	col = v2[1]
	if (grid[row][col] == 'r'):
		return 1
	if (grid[row][col] == 'f'):
		return 2
	if (grid[row][col] == 'h'):
		return 5
	if (grid[row][col] == 'm'):
		return 10
		

def a_star_search(grid, start, goal):
	frontier = PriorityQueue()
	frontier.put(start, 0)

	shortest_path = {}
	cost = {}
	shortest_path[start] = None
	cost[start] = 0

	while not frontier.empty():
		current = frontier.get()
		# print("Current: ", current)
        	
		if current == goal:
			break
        
		for next in neighbors(grid, current):
			new_cost = cost[current] + get_cost(grid, current, next)
			if next not in cost or new_cost < cost[next]:
				cost[next] = new_cost
				priority = new_cost + heuristic2(next, goal)	
				# print("-> Frontier: ",next,priority)
				frontier.put(next, priority)
				shortest_path[next] = current
	return shortest_path


def find_path(map_data, init_r, init_c, goal_r, goal_c):
	"""
	Find the lowest cost path
	Returns the path as a list
	"""
	start = (init_r, init_c)
	goal = (goal_r, goal_c)
	result = a_star_search(map_data, start, goal)
	# print (result)
	solution = convert(reconstruct(result, start, goal))
	# print(solution)
	return solution


def reconstruct(path, start, goal):
	new_path = []	
	current = goal
	while (current != None):
		new_path.insert(0, current)
		current = path[current]
	# print(new_path)
	return new_path


def convert(path):
	"""
	Converts a list of tuples into "d/u/l/r" chars
	Returns the new path as a list
	"""
	new_path = []
	for x in range(len(path)-1):
		row1 = path[x][0]
		col1 = path[x][1]
		row2 = path[x+1][0]
		col2 = path[x+1][1]
		if (row1 > row2):
			new_path.append('u')
		elif (row1 < row2):
			new_path.append('d')
		elif (col1 > col2):
			new_path.append('l')
		elif (col1 < col2):
			new_path.append('r')	
	return new_path


def main(argv=None):
	"""Main function"""

	# Read command line arguments
	mapfile = sys.argv[1]
	initial_row = int(sys.argv[2])
	initial_col = int(sys.argv[3])
	goal_row = int(sys.argv[4])
	goal_col = int(sys.argv[5])

	# Convert the mapfile into an appropriate data structure
	m = parse_map(mapfile)

	# Find the lowest cost path
	solution = find_path(m, initial_row, initial_col, goal_row, goal_col)
	print(solution)


# Run as: $ ./p1.py mapfile.txt init_row init_col goal_row goal_col
if __name__ == "__main__":
	main(sys.argv)

