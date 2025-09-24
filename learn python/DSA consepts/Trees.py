# Trees - Non linear data structure

#  becouse : The data in a tree are not stored in a sequential manner i.e.,
# they are not stored linearly. Instead

# The topmost node of the tree is called the root, and the nodes
#  below it are called the child nodes. Each node can have
#  multiple child nodes, and these child nodes can also have
#  their own child nodes, forming a recursive structure.


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


from collections import deque


# Function to add an edge between vertices x and y
def addEdge(x, y, adj):
    adj[x].append(y)
    adj[y].append(x)


# Function to print the parent of each node
def printParents(node, adj, parent):
    # current node is Root, thus, has no parent
    if parent == 0:
        print("{}--root".format(node))
    else:
        print("{}---{}(p)".format(node, parent))

    for cur in adj[node]:
        if cur != parent:
            printParents(cur, adj, node)


def printChildren(Root, adj):
    q = deque()
    # pushing root
    q.append(Root)
    # visit array to keep track of nodes that have been visted
    vis = [0] * len(adj)
    # BFS
    while q:
        node = q.popleft()
        vis[node] = 1
        print("{}->".format(node)),
        for cur in adj[node]:
            if vis[cur] == 0:
                print(cur),
                q.append(cur)
        print()


N = 7
Root = 1
# Adjacency list to store the tree
adj = [[] for _ in range(N + 1)]
# Creating the tree
addEdge(1, 2, adj)
addEdge(1, 3, adj)
addEdge(1, 4, adj)
addEdge(2, 5, adj)
addEdge(2, 6, adj)
addEdge(4, 7, adj)

# Printing the parents of each node
print("The parents of each node are:")
printParents(Root, adj, 0)


print("The children of each node are:")
printChildren(Root, adj)
