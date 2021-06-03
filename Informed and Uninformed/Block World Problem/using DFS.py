import copy


class Node:
    config = []
    parent = None

    def __init__(self, Config, Parent):
        self.config = Config
        self.parent = Parent

    def generate(self):  # returns a list containing the next set of moves from current state
        generated = []
        temp = copy.deepcopy(self.config)
        for x in temp:
            if len(x) == 1:  # if directly on table place on every other block
                temp2 = copy.deepcopy(temp)
                temp2.remove(x)
                for y in temp2 :    # all other stacks than the one in question
                    tempList = copy.deepcopy(temp2)
                    tempList.append(x+y)
                    tempList.remove(y)
                    generated.append(tempList)
            if len(x) > 1 : # if more than one blocks are encountered
                temp2 = copy.deepcopy(temp)
                index = temp2.index(x)
                topBlock = temp2[index].pop(0)
                for i in temp2 :
                    tempList = copy.deepcopy(temp2)
                    tempList.append([topBlock] + i)
                    tempList.remove(i)
                    generated.append(tempList)
                    if tempList==temp :
                        generated.remove(tempList)
                tempList = copy.deepcopy(temp2)
                tempList.append([topBlock])
                generated.append(tempList)
        return generated

    def getConfig(self):
        return self.config

    def getParent(self):
        return self.parent


class BlockProblem:
    stack = []
    visited = []

    def __init__(self, startingNode, endState):
        self.begin = startingNode
        self.end = [endState]

    def DFS(self):
        self.stack.append(self.begin)
        self.visited.append(self.begin.getConfig())
        self.run()

    def run(self):
        if len(self.stack) == 0:
            print("xxxxxx DFS ended stack reached zero xxxxxx")
            return
        currentNode = self.stack.pop(len(self.stack) - 1)  # pop top element from the stack
        print("processing : ")
        print(currentNode.getConfig())
        if currentNode.getConfig() == self.end:
            print("========GOAL REACHED========")
            self.traceParent(currentNode)
            return
        for i in currentNode.generate():
            x = Node(i,currentNode)
            if x not in self.stack:
                if x.getConfig() not in self.visited:
                    self.stack.append(x)
                    self.visited.append(x.getConfig())
        self.run()

    def traceParent(self, node):
        if node == None:
            return
        print(node.getConfig())
        print('^')
        self.traceParent(node.getParent())


initialConfig = []  # list of stacks
finalConfig = []
noStacks = int(input("Enter number of stacks in initial state : "))
for x in range(noStacks):
    print("enter stack number : " + str(x + 1))
    line = input().split()
    initialConfig.append(line)
print(initialConfig)
print("Enter final config : ")
line = input().split()
finalConfig = line
print(finalConfig)
starting = Node(initialConfig, None)
finder = BlockProblem(starting, finalConfig)
finder.DFS()
