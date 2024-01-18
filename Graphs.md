==Start with -1 as parent==
# Connected Components

Graph doesn't necessarily need to be connected (i.e if you start from one node you can reach all nodes) . 

![](Images/Pasted%20image%2020240109220912.png)

Above graph has 10 nodes and 8 edges and 4 different connected components. ==Therefore always run loop to Check all nodes==

```python
for i in range(10):
	if not visited[i]:
		traversal(i)
```
	
# BFS

![](Images/Pasted%20image%2020240110221636.png)

- ==Uses queue==
- **Time Complexity:** O(N) + O(2E), Where N = Nodes, 2E is for total degrees as we traverse all adjacent nodes.
- **Space Complexity:** O(3N) ~ O(N), Space for queue data structure visited array and an adjacency list
- ==Implementation usually involves loops==

```Python
# to print a BFS of a graph
def bfs(node):

    # mark vertices as False means not visited
    visited = [False] * (len(graph))

    # make an empty queue for bfs
    queue = []

    # mark gave node as visited and add it to the queue
    visited.append(node)
    queue.append(node)

    while queue:
        # Remove the front vertex or the vertex at the 0th index from the queue and print that vertex.
        v = queue.pop(0)
        print(v, end=" ")

        # Get all adjacent nodes of the removed node v from the graph hash table.
        # If an adjacent node has not been visited yet,
        # then mark it as visited and add it to the queue.
        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)
```

# DFS

![](Images/Pasted%20image%2020240114145354.png)

- ==Uses Stack==
- ==Implementation usually involves Recursion==
- Start with the root node in the stack. Pop the root, add its neighbors to the stack, and repeat until the stack is empty. For each new node:

1. Push it onto the stack.
2. Mark as visited.
3. For adjacent nodes:
    - If unvisited, visit them.
    - If no adjacent nodes, remove from the stack. Repeat these steps for each node, recursively exploring until a dead end is reached.

```Python

def dfs(node, graph, visited, component):
    component.append(node)  # Store answer
    visited[node] = True  # Mark visited

    # Traverse to each adjacent node of a node
    for child in graph[node]:
        if not visited[child]:  # Check whether the node is visited or not
            dfs(child, graph, visited, component)  # Call the dfs recursively

if __name__ == "__main__":

    # Graph of nodes
    graph = {
        0: [2],
        1: [2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    node = 0  # Starting node
    visited = [False]*len(graph)  # Make all nodes to False initially
    component = []
    dfs(node, graph, visited, component)  # Traverse to each node of a graph
    print(f"Following is the Depth-first search: {component}")  # Print the answer
```

# Detect Cycle

- ==Main idea Traverse and keep Track of parent node==
- ==If we Encounter a visited node that is not parent of current node, then cycle exists==
- ==Make sure to check for connected components==

## BFS Implementation

**Time Complexity**: O(N + 2E) + O(N), Where N = Nodes, 2E is for total degrees as we traverse all adjacent nodes. In the case of connected components of a graph, it will take another O(N) time.

**Space Complexity:** O(N) + O(N) ~ O(N), Space for queue data structure and visited array.

```Python 
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)  # As the graph is undirected

    def isCyclicConnectedComponent(self, s, visited):
        # Create a queue for BFS
        queue = deque()
        queue.append((s, -1))  # (node, parent)
        visited[s] = True

        while queue:
            vertex, parent = queue.popleft()

            # Check adjacent vertices
            for i in self.graph[vertex]:
                if not visited[i]:
                    visited[i] = True
                    queue.append((i, vertex))
                elif parent != i:
                    return True
        return False

    def isCyclic(self):
        visited = [False] * self.V

        # Call the helper function for all unvisited vertices to handle disconnected graph
        for i in range(self.V):
            if not visited[i]:
                if self.isCyclicConnectedComponent(i, visited):
                    return True
        return False

# Example Usage
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

if g.isCyclic():
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")

```

## DFS Implementation

**Time Complexity:** O(N + 2E) + O(N), Where N = Nodes, 2E is for total degrees as we traverse all adjacent nodes. In the case of connected components of a graph, it will take another O(N) time.

**Space Complexity:** O(N) + O(N) ~ O(N), Space for recursive stack space and visited array.

```Python
class Graph:
    def __init__(self, vertices):
        self.Vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, parent,visited):
        visited[v] = True

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.dfs(neighbour, v,visited):
                    return True
            elif parent != neighbour:
                return True

        return False

    def is_cyclic(self):
        visited = [False] * self.Vertices

        for i in range(self.Vertices):
            if not visited[i]:
                if self.dfs(i, -1,visited):
                    return True

        return False


# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 3)

if g.is_cyclic():
    print("Graph contains a cycle")
else:
    print("Graph does not contain a cycle")
```
