#!/usr/local/bin/python3
from typing import List
from collections import OrderedDict
class Graph(object):
    def __init__(self, edges):
        self.edges = OrderedDict()
        self.nodes = OrderedDict() 
        for a,b in edges:
            if a not in self.nodes:
                self.nodes[a] = Node()
                self.edges[a] = []
            self.edges[a].append(b)
            if b not in self.nodes:
                self.nodes[b] = Node()
                self.edges[b] = []
            self.edges[b].append(a)

class Node():
    def __init__(self):
        self.index = self.lowLink = None
        self.onstack = False

class Solution:
    stack = list()
    index = 0
    scc = OrderedDict()

    def strongConnect(self, node, preceedNode=None):
        _node = self.graph.nodes[node]
        _node.index = _node.lowLink = self.index
        self.index += 1
        self.stack.append(node)
        _node.onstack = True

        for b in self.graph.edges[node]:
            if b == preceedNode:
                continue
            nodeb = self.graph.nodes[b]
            if nodeb.index is None:
                self.strongConnect(b, node)
                _node.lowLink = min(_node.lowLink, nodeb.lowLink)
            elif nodeb.onstack:
                _node.lowLink = min(_node.lowLink, nodeb.index)

        if _node.index == _node.lowLink:
            self.scc[node] = scc = set()
            while len(self.stack):
                cur = self.stack.pop()
                scc.add(cur)
                if cur == node:
                    break

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.graph = Graph(connections)
        # print(self.graph.nodes)
        # print(self.graph.edges)
        for node in range(n):
            if self.graph.nodes[node].index == None:
                self.strongConnect(node)
        print(self.scc)
        criticalEdges = []
        for c in connections:
            for scc in self.scc.values():
                if set(c).issubset(scc):
                    break
            else:
                criticalEdges.append(c)
        return criticalEdges

nets = [(4, [[0,1],[1,2],[2,0],[1,3]]),
        (5, [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]),
        (6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]])
        ]
for nodes, connections in nets:
    s = Solution()
    print(s.criticalConnections(nodes, connections))
