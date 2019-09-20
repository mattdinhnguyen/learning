# Given a singly linked list where elements are 
# sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree 
# is defined as a binary tree in which the depth 
# of the two subtrees of every node never differ by more than 1.
# Given the sorted linked list: [-10,-3,0,5,9],
# -10
#   \
#   -3
#    \
#     0
#      \
#      5
#       \
#        9

#     0
#    / \
#  -3   5
#  /     \
# -10     9

#     0
#    / \
#  -3   9
#  /   /
# -10  5


#     -3
#    / \
#  -10   5
#       / \
#      0   9

#      5
#    /  \
#   -3   9
#  /  \
# -10  0 
# Solution: https:#leetcode.com/problems/convert-sorted-list-to-binary-search-tree
from treeUtil import showRel, showRelations, childs, Node

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def Lst2LinkLst(lst, idx):
    head = node = ListNode(lst[idx])
    for i in lst[idx+1:]:
        node.next = ListNode(i)
        node = node.next
    return head

List = [-10,-3,0,5,9]
Head = Lst2LinkLst(List, 0)

def showLinkLst(h):
    while h:
        print(h.val),
        h = h.next
    print("\n")

showLinkLst(Head)

class Solution:
    def __init__(self, lstHead):
        self.head = lstHead
        self.root = Node(self.head.val)

    def sortedListToBST(self):
        r = self.root
        h = self.head.next
        count = 1
        while h:
            r.right = Node(h.val)
            r = r.right
            h = h.next
            count += 1
        r = self.root
        for _ in range((count/2)-1):
            r = r.right
        r.right.left = self.root
        self.root = r.right
        r.right = None
        return self.root

    def showTree(self, root):
        print(showRel(root))
        children = childs([root])
        while children:
            print(showRelations(children))
            children = childs(children)

s = Solution(Head)
r = s.sortedListToBST()
s.showTree(r)