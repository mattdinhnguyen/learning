
class Node(object):
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

def showRel(n):
    leftV = n.left and str(n.left.v) or "None"
    rightV = n.right and str(n.right.v) or "None"
    return "{}---{}---{}".format(leftV,n.v,rightV)

def showRelations(lst):
    oStr = ""
    for node in lst:
        oStr += showRel(node) + "    "
    return oStr

def childs(lst):
    def _childs(n):
        return [n.left,n.right]
    children = []
    for n in lst:
        if n.left and any(_childs(n.left)):
            children.append(n.left)
        if n.right and any(_childs(n.right)):
            children.append(n.right)
    return children
