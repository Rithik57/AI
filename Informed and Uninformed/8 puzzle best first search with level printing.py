import copy


class Node:
    def __init__(self, Config, Parent):
        self.config = Config
        self.parent = Parent

    def getConfig(self):
        return self.config

    def getParent(self):
        return self.parent

    def generateMoves(self):
        generated = []
        for i in range(3):
            for j in range(3):
                if self.config[i][j] == 0:
                    pos = (i, j)  # pos tuple stores the row and column for the empty tile

        temp = copy.deepcopy(self.config)
        self.left(temp, pos)
        generated.append(temp)
        temp = copy.deepcopy(self.config)
        self.right(temp, pos)
        generated.append(temp)
        temp = copy.deepcopy(self.config)
        self.up(temp, pos)
        generated.append(temp)
        temp = copy.deepcopy(self.config)
        self.down(temp, pos)
        generated.append(temp)

        return generated

    # helper functions
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


class Puzzle:
    def __init__(self, starting, ending):
        self.begin = starting  # node to begin from
        self.goal = ending  # goal configuration
        self.heuristics = {}  # stores heuristics corresponding to states
        self.visited = []  # tracks the configurations already visited
        self.nodeCreated  =0

    def bestFirstSearch(self):
        self.heuristics[self.begin] = self.getHeuristic(self.begin.getConfig())
        self.visited.append(self.begin.getConfig())
        self.run()

    def run(self):
        self.nodeCreated +=1
        if len(self.heuristics) == 0:
            return
        min = 1000
        for x in self.heuristics.keys() :
            if self.heuristics[x] < min :
                min = self.heuristics[x]
                best = x
        current = copy.deepcopy(best)
        self.heuristics.pop(best)
        if current.getConfig() == self.goal:  # if goal is found then end the search
            print("==================GOAL FOUND==================")
            self.traceParent(current)
            print("__________MOVES MADE : "+str(self.nodeCreated-1)+"__________")
            return
        # if goal not found then generate further nodes
        for x in current.generateMoves():
            node = Node(x, current)
            if node not in self.heuristics.values():
                if node.getConfig() not in self.visited:
                    self.heuristics[node] = self.getHeuristic(node.getConfig())
        self.run()

    def traceParent(self, node):
        if node == None:
            return
        for x in node.getConfig():
            print(x)
        print()
        print('^')
        self.traceParent(node.getParent())

    def getHeuristic(self, matrix):  # returns the heuristic of the given configuration
        # compare the tiles with the positions in the goal state
        counter = 0
        for i in range(3):
            for j in range(3):
                if matrix[i][j] != self.goal[i][j]:
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
startObject = Node(starting,None)
print("Enter goal configuration")
goal = [[0 for row in range(3)] for column in range(3)]
for i in range(3):
    first = input(str(i + 1) + " row of initial config : ").split()
    for x in range(3):
        goal[i][x] = int(first[x])
# create runner object and start search
finder = Puzzle(startObject,goal)
finder.bestFirstSearch()
