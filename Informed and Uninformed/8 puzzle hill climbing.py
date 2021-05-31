import copy


class Graph:
    visited = list()  # list to mark visited states
    moveCounter = 0
    heuristics = {}  # mapping the states with heuristics

    def __init__(self, starting, goal):
        # set the starting and goal state for the search
        self.begin = starting
        self.end = goal

    def start(self):
        # add the starting state to the mapping and run the search
        self.heuristics[self.getHeuristic(self.begin)] = self.begin
        traversal = self.run()
        print("number of moves made : " + str(self.moveCounter))
        print("traversal is : ")
        for x in traversal:
            for i in x:
                print(i)
            print()

    def run(self):
        # if the queue is empty then end the search
        if len(self.heuristics) == 0:
            print("local maxima has occured")
            return self.visited
        # get the first value from the dictionary
        best = self.heuristics[list(self.heuristics.keys())[0]]
        current = copy.deepcopy(best)
        self.moveCounter += 1  # increment moveCounter as more elements are processed
        if current not in self.visited:  # if the state has not already been visited then add
            self.visited.append(current)

        # if this the goal state then end the search
        if current == self.end:
            return self.visited
        # find the position of empty tile
        for i in range(3):
            for j in range(3):
                if current[i][j] == 0:
                    pos = (i, j)  # pos tuple stores the row and column for the empty tile
        # perform all legal moves on this state and add to queue
        temp = copy.deepcopy(current)  # creating a deepcopy of the current matrix to operate

        # only add the values that have a better heuristic than the current state
        self.left(temp, pos)
        if temp not in self.visited and temp not in self.heuristics.values():
            if self.getHeuristic(temp) <= list(self.heuristics.keys())[0]:
                self.heuristics[self.getHeuristic(temp)] = temp

        temp = copy.deepcopy(current)
        self.right(temp, pos)
        if temp not in self.visited and temp not in self.heuristics.values():
            if self.getHeuristic(temp) <= list(self.heuristics.keys())[0]:
                self.heuristics[self.getHeuristic(temp)] = temp

        temp = copy.deepcopy(current)
        self.up(temp, pos)
        if temp not in self.visited and temp not in self.heuristics.values():
            if self.getHeuristic(temp) <= list(self.heuristics.keys())[0]:
                self.heuristics[self.getHeuristic(temp)] = temp

        temp = copy.deepcopy(current)
        self.down(temp, pos)
        if temp not in self.visited and temp not in self.heuristics.values():
            if self.getHeuristic(temp) <= list(self.heuristics.keys())[0]:
                self.heuristics[self.getHeuristic(temp)] = temp

        self.heuristics.pop(list(self.heuristics.keys())[0])
        # recursively running the search for the updated queue
        return self.run()

    # helper functions to move the empty tile
    def left(self, matrix, pos):
        if pos[1] != 0:
            temp = matrix[pos[0]][pos[1]]
            matrix[pos[0]][pos[1]] = matrix[pos[0]][pos[1] - 1]
            matrix[pos[0]][pos[1] - 1] = temp

    def right(self, matrix, pos):
        if pos[1] != 2:
            temp = matrix[pos[0]][pos[1]]
            matrix[pos[0]][pos[1]] = matrix[pos[0]][pos[1] + 1]
            matrix[pos[0]][pos[1] + 1] = temp

    def up(self, matrix, pos):
        if pos[0] != 0:
            temp = matrix[pos[0]][pos[1]]
            matrix[pos[0]][pos[1]] = matrix[pos[0] - 1][pos[1]]
            matrix[pos[0] - 1][pos[1]] = temp

    def down(self, matrix, pos):
        if pos[0] != 2:
            temp = matrix[pos[0]][pos[1]]
            matrix[pos[0]][pos[1]] = matrix[pos[0] + 1][pos[1]]
            matrix[pos[0] + 1][pos[1]] = temp

    # returns an integer as the heuristic value for a matrix
    def getHeuristic(self, matrix):

        # compare the tiles with the positions in the goal state
        counter = 0
        for i in range(3):
            for j in range(3):
                if matrix[i][j] != self.end[i][j]:
                    counter += 1
        return counter


# main function
# initializing matrices and entering values for start and goal state
starting = [[0 for row in range(3)] for column in range(3)]
print("Enter initial configuration")
for i in range(3):
    first = input(str(i + 1) + " row of initial config : ").split()
    for x in range(3):
        starting[i][x] = int(first[x])
print("Enter goal configuration")
goal = [[0 for row in range(3)] for column in range(3)]
for i in range(3):
    first = input(str(i + 1) + " row of initial config : ").split()
    for x in range(3):
        goal[i][x] = int(first[x])
# create runner object and start search
graph = Graph(starting, goal)
graph.start()
