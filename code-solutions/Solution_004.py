from copy import deepcopy

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    node = deepcopy(root_node)

    while(node):
        if(k < node.value):
            ceil = node.value
            node = node.left
        elif(k > node.value):
            floor = node.value
            node = node.right
        else:
            floor = node.value
            ceil = node.value
            break

    return (floor, ceil)


def findCeilingRec(root_node, k):
    if(not root_node):
        return -1

    if(k > root_node.value):
        return findCeilingRec(root_node.right, k)

    if(k < root_node.value):
        ceil = findCeilingRec(root_node.left, k)
        if(k <= ceil):
            return ceil
        return root_node.value
    
    return root_node.value


def findFloorRec(root_node, k):
    if(not root_node):
        return -1

    if(k > root_node.value):
        floor = findFloorRec(root_node.right, k)
        if(floor <= k):
            return floor
        return root_node.value

    if(k < root_node.value):
        return findFloorRec(root_node.left, k)
    
    return root_node.value



if(__name__ == "__main__"):
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)

    root.left.left = Node(2)
    root.left.right = Node(6)

    root.right.left = Node(10)
    root.right.right = Node(14)

    for i in range(16):
        print(f"i = {i} | {findCeilingFloor(root, i)}")