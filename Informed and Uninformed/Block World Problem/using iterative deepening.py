import copy


class Node:
    config = []
    parent = None
    level = -1

    def __init__(self, Config, Parent,Level):
        self.config = Config
        self.parent = Parent
        self.level = Level

    def generate(self):  # todo : generate a list containing the next set of moves
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

    def getLevel(self):
        return self.level


class BlockProblem:
    moveCounter =0
    stack = []
    visited = []

    def __init__(self, startingNode, endState, depthLevel):
        self.begin = startingNode
        self.end = [endState]
        self.depthLevel = depthLevel
        self.stack= []
        self.visited = []
        print("============= max depth level is : "+str(depth)+" =============")

    def DFS(self):
        self.stack.append(self.begin)
        self.visited.append(self.begin.getConfig())
        self.run()

    def run(self):
        self.moveCounter +=1
        if len(self.stack) == 0:
            print("xxxxxx DFS ended queue reached zero xxxxxx")
            return False
        currentNode = self.stack.pop(len(self.stack) - 1)  # pop top element from the stack
        print("processing : ")
        for x in currentNode.getConfig() :
            for i in x :
                print(i,end=" ")
            print()
        print("at level "+str(currentNode.getLevel()))
        if currentNode.getConfig() == self.end:
            print("========GOAL REACHED========")
            self.traceParent(currentNode)
            quit()
            return True
        for i in currentNode.generate():
            currentLevel = currentNode.getLevel()
            x = Node(i,currentNode,currentLevel+1)
            if x not in self.stack:
                if x.getConfig() not in self.visited:
                    if x.getLevel() <=  self.depthLevel :
                        self.stack.append(x)
                        self.visited.append(x.getConfig())
        self.run()

    def traceParent(self, node):
        if node == None:
            print("___________ no of moves made : "+str(self.moveCounter)+" ___________")
            return
        for x in node.getConfig():
            for i in x:
                print(i, end=" ")
            print()
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
starting = Node(initialConfig, None,0)
depth = 1
while True:
    finder = BlockProblem(starting,finalConfig,depth)
    finder.DFS()
    depth+=1
    if depth == 10:
        break
