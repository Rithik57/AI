import copy


class Node:

    def __init__(self, config, level, parent):
        self.config = config
        self.level = level
        self.parent = parent

    def getParent(self):
        return self.parent

    def getLevel(self):
        return self.level

    def getConfig(self):
        return self.config

    def printInfo(self):
        print(self.config)
        print(self.level)
        print(self.parent)

    def printConfig(self):
        for x in self.config:
            print(x)


class Graph:
    visited = list()  # list to mark visited states
    moveCounter = 0
    heuristics = {}  # mapping the states with heuristics

    def __init__(self, starting, goal):
        # set the starting and goal state for the search
        self.begin = Node(starting,0,None)
        self.end = goal

    def start(self):
        # add the starting state to the mapping and run the search
        self.heuristics[self.getScore(self.begin)] = self.begin
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
            print("heuristic dictionary was emptied ending search")
            return
        # get the value corresponding to the best heuristic key from the mapping
        best = self.heuristics[sorted(self.heuristics.keys())[0]]
        current = copy.deepcopy(best)
        # remove this value from the mapping
        self.heuristics.pop(sorted(self.heuristics.keys())[0])
        self.moveCounter += 1  # increment moveCounter as more elements are processed
        if current.getConfig() not in self.visited:  # if the state has not already been visited then add
            self.visited.append(current.getConfig())
        # if this the goal state then end the search
        if current.getConfig() == self.end:
            print("goal state found")
            self.getSubtree(current)
            return self.visited
        # find the position of empty tile
        for i in range(3):
            for j in range(3):
                if current.getConfig()[i][j] == 0:
                    pos = (i, j)  # pos tuple stores the row and column for the empty tile
        # perform all legal moves on this state and add to queue
        tempConfig = copy.deepcopy(current.getConfig())  # creating a deepcopy of the current matrix to operate
        temp = Node(tempConfig,current.getLevel()+1,current)
        self.left(temp, pos) #creates the childs configuration
        if temp.getConfig() not in self.visited and temp not in self.heuristics.values():
            self.heuristics[self.getScore(temp)] = temp

        tempConfig = copy.deepcopy(current.getConfig())  # creating a deepcopy of the current matrix to operate
        temp = Node(tempConfig, current.getLevel() + 1, current)
        self.right(temp, pos)
        if temp.getConfig() not in self.visited and temp not in self.heuristics.values():
            self.heuristics[self.getScore(temp)] = temp

        tempConfig = copy.deepcopy(current.getConfig())  # creating a deepcopy of the current matrix to operate
        temp = Node(tempConfig, current.getLevel() + 1, current)
        self.up(temp, pos)
        if temp.getConfig() not in self.visited and temp not in self.heuristics.values():
            self.heuristics[self.getScore(temp)] = temp

        tempConfig = copy.deepcopy(current.getConfig())  # creating a deepcopy of the current matrix to operate
        temp = Node(tempConfig, current.getLevel() + 1, current)
        self.down(temp, pos)
        if temp.getConfig() not in self.visited and temp not in self.heuristics.values():
            self.heuristics[self.getScore(temp)] = temp

        # recursively running the search for the updated queue
        return self.run()

    # helper functions to move the empty tile
    def left(self, node, pos):
        matrix = node.getConfig()
        if pos[1] != 0:
            temporary = matrix[pos[0]][pos[1]]
            matrix[pos[0]][pos[1]] = matrix[pos[0]][pos[1] - 1]
            matrix[pos[0]][pos[1] - 1] = temporary

    def right(self, node, pos):
        matrix = node.getConfig()
        if pos[1] != 2:
            temp = matrix[pos[0]][pos[1]]
            matrix[pos[0]][pos[1]] = matrix[pos[0]][pos[1] + 1]
            matrix[pos[0]][pos[1] + 1] = temp

    def up(self, node, pos):
        matrix = node.getConfig()
        if pos[0] != 0:
            temp = matrix[pos[0]][pos[1]]
            matrix[pos[0]][pos[1]] = matrix[pos[0] - 1][pos[1]]
            matrix[pos[0] - 1][pos[1]] = temp

    def down(self, node, pos):
        matrix = node.getConfig()
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

    def getScore(self,node):
        Hscore = self.getHeuristic(node.getConfig())
        Gscore = node.getLevel()
        return Hscore+Gscore

    def getSubtree(self,node):
        if node==None :
            return
        node.printConfig()
        print("^")
        self.getSubtree(node.getParent())



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
