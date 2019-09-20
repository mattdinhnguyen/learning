#!/usr/local/bin/python3

BLACK = "B"
RED = "R"
Root = None
class Node(object):
    def __init__(self, val, color=BLACK, parent=None, left=None, right=None):
        self.value = val
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right
        self.count = 1

    def AddNode(self, node):
        self.count += 1
        if node.value >= self.value:
            if self.right:
                self.right.AddNode(node)
            else:
                self.right = node
                node.parent = self
                node.color = RED
                if self.color == RED:
                    self.re_balance(node)
        else:
            if self.left:
                self.left.AddNode(node)
            else:
                self.left = node
                node.parent = self
                node.color = RED
                if self.color == RED:
                    self.re_balance(node)

    def re_balance(self, node):
        parent = self
        value = node.value
        if (parent.parent is None  # parent is the root
           or BLACK in (node.color, parent.color)):  # no need to rebalance
            return
        grandfather = parent.parent
        node_dir = 'L' if parent.value > value else 'R'
        parent_dir = 'L' if grandfather.value > parent.value else 'R'
        uncle = grandfather.right if parent_dir == 'L' else grandfather.left
        general_direction = node_dir + parent_dir

        if uncle == None or uncle.color == BLACK:
            # rotate
            if general_direction == 'LL':
                self._right_rotation(node, parent, grandfather, to_recolor=True)
            elif general_direction == 'RR':
                self._left_rotation(node, parent, grandfather, to_recolor=True)
            elif general_direction == 'LR':
                self._right_rotation(node=None, parent=node, grandfather=parent)
                # due to the prev rotation, our node is now the parent
                self._left_rotation(node=parent, parent=node, grandfather=grandfather, to_recolor=True)
            elif general_direction == 'RL':
                self._left_rotation(node=None, parent=node, grandfather=parent)
                # due to the prev rotation, our node is now the parent
                self._right_rotation(node=parent, parent=node, grandfather=grandfather, to_recolor=True)
            else:
                raise Exception("{} is not a valid direction!".format(general_direction))
        else:  # uncle is RED
            self._recolor(grandfather)

    def __update_parent(self, node, parent_old_child, new_parent):
        """
        Our node 'switches' places with the old child
        Assigns a new parent to the node.
        If the new_parent is None, this means that our node becomes the root of the tree
        """
        node.parent = new_parent
        if new_parent:
            # Determine the old child's position in order to put node there
            if new_parent.value >= parent_old_child.value:
                new_parent.left = node
            else:
                new_parent.right = node
        else:
            global Root
            Root = node

    def _right_rotation(self, node, parent, grandfather, to_recolor=False):
        grand_grandfather = grandfather.parent
        self.__update_parent(node=parent, parent_old_child=grandfather, new_parent=grand_grandfather)

        old_right = parent.right
        parent.right = grandfather
        grandfather.parent = parent

        grandfather.left = old_right  # save the old right values
        if old_right:
            old_right.parent = grandfather

        if to_recolor:
            parent.color = BLACK
            node.color = RED
            grandfather.color = RED

    def _left_rotation(self, node, parent, grandfather, to_recolor=False):
        grand_grandfather = grandfather.parent
        self.__update_parent(node=parent, parent_old_child=grandfather, new_parent=grand_grandfather)

        old_left = parent.left
        parent.left = grandfather
        grandfather.parent = parent

        grandfather.right = old_left  # save the old left values
        if old_left:
            old_left.parent = grandfather

        if to_recolor:
            parent.color = BLACK
            node.color = RED
            grandfather.color = RED

    def _recolor(self, grandfather):
        grandfather.right.color = BLACK
        grandfather.left.color = BLACK
        if grandfather != Root:
            grandfather.color = RED
        self.re_balance(grandfather)

    def find_node(self, value):
        def inner_find():
            if value > self.value:
                return self.right and self.right.find_node(value)
            elif value < self.value:
                return self.left and self.left.find_node(value)
            else:
                return self

        found_node = inner_find()
        return found_node

    def edges(self):
        descendants = []
        for c in self.children():
            descendants.append((self.value, c.value))
            descendants.extend(c.edges())
        return descendants

    def alias(self):
        return str(self.value) + self.color

    def __iter__(self):
        if self.left:
            yield from self.left.__iter__()
        yield self.alias()
        if self.right:
            yield from self.right.__iter__()

    def children(self):
        return [c for c in [self.left, self.right] if c]

    def _children(self, clist):
        g = []
        cls = []
        for c in clist:
            if c:
                cls.append(str(c.value)+c.color)
                if c.left:
                    g.append(c.left)
                else:
                    g.append(None)
                if c.right:
                    g.append(c.right)
                else:
                    g.append(None)
            else:
                cls.append("None")
        if [_g for _g in g if _g != None]:
            return  "  ".join(cls) + "\n" + self._children(g)
        else:
            return "  ".join(cls)
 
    def __str__(self):
        return "{}{}\n{}".format(self.value, self.color, self._children([self.left,self.right]))

def L2bst(l):
    global Root
    Root = Node(l[0])
    for el in l[1:]:
        Root.AddNode(Node(el))

import random
random.seed(0)
#random_list = [random.randint(1, 1000) for _ in range(100)]
#random_list = [random.randint(1, 10) for _ in range(10)]
random_list = [9, 8, 5, 3, 6, 5, 8, 4, 5, 6]
print(random_list)
L2bst(random_list)
'''
      __________8B__________
_____5R_____        _____9B_____
3B__     __5R__    8R          None
   4R   5B    6B__
                 6R
'''
print(Root)
print(Root.edges())
print(list(Root))
