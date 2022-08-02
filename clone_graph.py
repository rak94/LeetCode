# initialize a node
class Node:
    def __init__(self, val= 0, neighbors = None):
        self.val = val
    
class CloneGraph:
    def cloning(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)