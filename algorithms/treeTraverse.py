# Traversing the tree
# Iterative, breadth-first search, level order traversal [6, 4, 3, 9, 1, null, 8]
# Recursive, depth-first search
# [6, 4, 9, 1, 3, null, 8] pre order
# [9, 4, 1 , 6, null, 3, 8] in order
# [9, 1, 4, null, 8, 3, 6] post order
#        6
#      /   \
#     4      3
#    /\      /\  
#   9  1  null 8
import sys
from treeUtil import Node, showRel, showRelations, childs

# levelOrderList = [6, 4, 3, 9, 1, None, 8]
#        6
#      /   \
#     4      3
#    /\       \  
#   -9  1       8
#   /
# 100
# levelOrderList = [6, 4, 3, -9, 1, None, 8, 100]
#        6
#          \
#            3
#            \  
#             1
#              \
#              100

levelOrderList = [6, None, 3, None, None, None, 1, None, None, None, None, None, None, None, 100]

root = Node(levelOrderList[0])
ln = len(levelOrderList)
def children(arr, lst):
    nextlst = []
    for idx, n in lst:
        l = idx*2 + 1
        if l < ln and arr[l] != None:
            n.left = Node(arr[l])
            nextlst.append((l, n.left))
        r = idx*2 + 2
        if r < ln and arr[r] != None:
            n.right = Node(arr[r])
            nextlst.append((r,n.right))
    if nextlst:
        children(arr, nextlst)

children(levelOrderList, [(0, root)])

print(showRel(root))
children = childs([root])
while children:
    print(showRelations(children))
    children = childs(children)

# level order traversal
def bfs(nodes):
    vals = []
    children = []
    for n in nodes:
        if n:
            vals.append(n.v)
            if any((n.left, n.right)):
               children.extend([n.left, n.right])
        else:
            vals.append(n)
    if children:
        return vals + bfs(children)
    else:
        return vals
 
print(bfs([root]))

def preOrderT(n):
    if n.left == n.right == None:
        return [n.v]
    elif not n.left:
        return [n.v, None] + preOrderT(n.right)
    elif not n.right:
        return [n.v] + preOrderT(n.left)
    else:
        return [n.v] + preOrderT(n.left) + preOrderT(n.right)

print(preOrderT(root))

def inOrderT(n):
    if n.left == n.right == None:
        return [n.v]
    elif not n.left:
        return [None, n.v] + inOrderT(n.right)
    elif not n.right:
        return preOrderT(n.left) + [n.v, None]
    else:
        return inOrderT(n.left) + [n.v] + inOrderT(n.right)

print(inOrderT(root))

def postOrderT(n):
    if n.left == n.right == None:
        return [n.v]
    elif not n.left:
        return [None] + postOrderT(n.right) + [n.v]
    elif not n.right:
        return postOrderT(n.left) + [None] + [n.v]
    else:
        return postOrderT(n.left) + postOrderT(n.right) + [n.v]

print(postOrderT(root))
# Given a binary tree in which each node 
# element contains a number. Find the maximum 
# possible sum from one leaf node to another.
def maxSumUntilNode(node, currentMax):
    if node == None:
        return 0
    elif node.left == node.right == None:
        return node.v
    elif node.left and node.right:
        maxLeft = maxSumUntilNode(node.left, currentMax)
        maxRight = maxSumUntilNode(node.right, currentMax)
        currentMax["val"] = max(currentMax["val"], maxLeft+maxRight+node.v)
        return max(maxLeft,maxRight) + node.v
    elif not node.left:
        return maxSumUntilNode(node.right, currentMax) + node.v
    elif not node.right:
        return maxSumUntilNode(node.left, currentMax) + node.v
        

maxVal = dict(val=-sys.maxsize-1)
maxSumUntilNode(root, maxVal)
print(maxVal["val"])
