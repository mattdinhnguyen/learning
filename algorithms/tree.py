# Given inorder and postorder traversal of a tree, construct the binary tree.
# inorderInput = [9,3,15,20,7]   # left, parent, right
# postorderInput = [9,15,7,20,3] # left, right, parent

#      3
#     / \
#    9   20
#        /\
#      15  7
from treeUtil import Node, showRel, showRelations, childs

inorderInput = [9,3,15,20,7] # left,root,right
postorderInput = [9,15,7,20,3] # left,right,root

def makeTree(inOrder,postOrder):
    if len(inOrder) == 0:
        return None
    rootV = postOrder[-1]
    rootIndex = inOrder.index(rootV)
    root = Node(rootV)
    root.left = makeTree(inOrder[:rootIndex], postOrder[:rootIndex])
    root.right = makeTree(inOrder[rootIndex+1:], postOrder[rootIndex:-1])
    return root

root = makeTree(inorderInput, postorderInput)

print(showRel(root))
children = childs([root])
while children:
    print(showRelations(children))
    children = childs(children)
