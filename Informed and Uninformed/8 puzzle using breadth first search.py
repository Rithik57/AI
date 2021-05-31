import copy


class Graph:
    queue = list()  # queue to mark which state to visit next
    visited = list()  # list to mark visited states
    moveCounter = 0

    def __init__(self, starting, goal):
        # set the starting and goal state for the search
        self.begin = starting
        self.end = goal

    def start(self):
        # add the starting state to the queue and run the search
        self.queue.append(self.begin)
        traversal = self.run()
        print("number of moves made : " + str(self.moveCounter))
        print("traversal is : ")
        for x in traversal:
            for i in x:
                print(i)
            print()

    def run(self):
        # if the queue is empty then end the search
        if len(self.queue) == 0:
            return
        # get the first element from the queue
        current = self.queue.pop(0)
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
        self.left(temp, pos)
        if temp not in self.visited and temp not in self.queue:
            self.queue.append(temp)
        temp = copy.deepcopy(current)
        self.right(temp, pos)
        if temp not in self.visited and temp not in self.queue:
            self.queue.append(temp)
        temp = copy.deepcopy(current)
        self.up(temp, pos)
        if temp not in self.visited and temp not in self.queue:
            self.queue.append(temp)
        temp = copy.deepcopy(current)
        self.down(temp, pos)
        if temp not in self.visited and temp not in self.queue:
            self.queue.append(temp)
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
