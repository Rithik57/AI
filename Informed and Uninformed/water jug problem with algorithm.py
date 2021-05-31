visited = list()
large = int(input("Enter the capacity of larger jug : "))
small = int(input("Enter the capacity of smaller jug : "))
req = int(input("Enter the required capacity : "))


def Pour(v1, v2):
    if v1 == req or v2 == req:  # if this the required state then return
        return visited
    if v2 == 0:  # if smaller jug is empty fill it
        v2 = small
        visited.append((v1, v2))
        return Pour(v1, v2)
    if v1 == large:  # if larger jug is full then empty it
        v1 = 0
        visited.append((v1, v2))
        return Pour(v1, v2)
    else:  # else transfer from smaller jug to larger jug
        if (large - v1) >= v2:
            v1 = v1 + v2
            v2 = 0
            visited.append((v1, v2))
            return Pour(v1, v2)
        else:
            v2 = v2 - (large - v1)
            v1 = large
            visited.append((v1, v2))
            return Pour(v1, v2)


v1 = 0
v2 = 0
print(Pour(v1, v2))
