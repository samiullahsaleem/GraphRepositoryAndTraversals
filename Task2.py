# Name: Sami Ullah Saleem
# Roll Number: BITF20M012

from collections import defaultdict # Import defaultdict from collections module to use it as a default dictionary

class Graph: 
    def __init__(self):
        self.graph = defaultdict(list) # default dictionary to store graph and list here is used to store the adjacent nodes of each node
        self.parent = defaultdict(lambda: None) # default dictionary to store parent of each node 
        self.level = defaultdict(lambda: 0) # default dictionary to store level of each node 
        self.color = defaultdict(lambda: "white") # default dictionary to store color of each node

    def addEdge(self, u, v):
        self.graph[u].append(v) # Add v to u's list of neighbours where u is the key and v is the value in the dictionary and u is parent of v 
        self.parent[v] = u # Add u as parent of v 
        self.level[v] = self.level[u] + 1 # Add level of v as level of u + 1
        self.color[v] = "white" # Add color of v as white

    def DFS(self, v, visited, parent, level): # DFS algorithm  where v is the node to start from, visited is a dictionary to store the visited nodes, parent is the parent of v and level is the level of v
        self.parent[v] = parent # Add parent of v as parent 
        self.level[v] = level # Add level of v as level
        self.color[v] = "gray" # Add color of v as gray
        visited[v] = "gray" # Mark the node as visited

        print(f"{v}", end = "->")

        # If you want to see the color, parent and level of each node, uncomment the following lines
        # print(f"{v}: color = gray, parent = {self.parent[v]} , level = {self.level[v]}")

        for i in self.graph[v]:
            if visited[i] == "white":
                self.DFS(i, visited, v, level + 1)

        visited[v] = "black"
        self.color[v] = "black"

        # If you want to see the color, parent and level of each node, uncomment the following lines
        # print(f"{v}: color = black, parent = {self.parent[v]} , level = {self.level[v]}")

    def BFS(self, v):
        visited = defaultdict(lambda: "white")
        queue = []
        visited[v] = "gray"
        queue.append((v, None, 0)) 

        while queue: # While the queue is not empty
            node, self.parent, self.level = queue.pop(0) # Pop the first element from the queue and assign it to node, parent and level of the node where node is the node, parent is the parent of the node and level is the level of the node
            print(f"{self.parent}->{node}") # Print the parent and the node (the node is the current node and the parent is the parent of the current node)

            # If you want to see the color, parent and level of each node, uncomment the following lines    
            #print(f"{node}: color = gray, parent = {self.parent}, level = {self.level}")

            for i in self.graph[node]: # For each node connected to the current node (node) in the graph (self.graph) 
                if visited[i] == "white":
                    visited[i] = "gray"
                    queue.append((i, node, self.level + 1)) # Add the node to the queue and add the parent of the node and the level of the node as the parent and the level of the node + 1

            visited[node] = "black" # Mark the node as visited
            # If you want to see the color, parent and level of each node, uncomment the following lines
            # print(f"{node}: color = black, parent = {self.parent}, level = {self.level}") # Print the node, its color, parent and level


def DFSandBFSOnAdjacentList():
    with open("Adjacency_list.txt", "r") as f:
        numberOfGraphs = int(f.readline().strip())
        for i in range(numberOfGraphs):
            g = Graph()
            nodes = []
            connections = []
            line = f.readline().strip()
            count = 1
            startingNode = None
            try: 
                while line != '*********':
                    try:
                        node, connections = line.split('\t')
                    except:
                        node = line
                        connections = 'None'
                    if count == 1:
                        startingNode = node
                        count += 1
                    nodes.append(node)
                    connections = connections.replace(' ', '')
                    connections = connections.split(',')
                    for j in range(len(connections)):
                        g.addEdge(node, connections[j])
                    line = f.readline().strip()
            except:
                    print("An Exception occur from your side. Please check your file and try again")
            print(f"DFS on Graph {i + 1}:")
            visited = defaultdict(lambda: "white") # white - not visited, gray - visited, black - finished visiting all the nodes connected to it  
            g.DFS(str(startingNode), visited, None, 0) # DFS algorithm starting from the first node in the graph (0) and None as parent and level 0 
            print(f"None\nBFS on Graph {i + 1}:")
            g.BFS(str(startingNode)) # BFS algorithm starting from the first node in the graph (0
            count = 1
            startingNode = None
    f.close()
def DFSandBFSOnAdjacentMatrix():
    with open("Adjacency_Matrix.txt", "r") as f:
        num_graphs = int(f.readline().strip()) # Read the first line and convert it to an integer (the number of graphs) and strip the newline character from the end of the line (if there is one)
        for i in range(num_graphs): # For each graph in the file (the number of graphs is given in the first line of the file) 
            graphNumber = i + 1 # The number of the graph (used for printing purposes)
            g = Graph()
            # Read the nodes and adjacency matrix
            nodes = [] # Create an empty list to store the nodes of the graph in (the nodes are the first line of the graph) 
            AdjacentMatrix = [] # Create an empty list to store the adjacency matrix of the graph in (the adjacency matrix is the second line of the graph) 
            line = f.readline().strip() # Read the first line of the graph and strip the newline character from the end of the line (if there is one)
            count = 1
            startingNode = None
            while line != '*********':
                node, connections = line.split('\t') # Split the line into the node and the connections (the connections are separated by a tab character)
                if count == 1:
                    startingNode = node
                    count += 1
                nodes.append(node) # Add the node to the list of nodes of the graph 
                AdjacentMatrix.append([int(x) for x in connections.split(',')]) # Add the connections to the adjacency matrix of the graph (the connections are separated by a comma character)
                line = f.readline().strip() # Read the next line of the graph and strip the newline character from the end of the line (if there is one)
            # Print the edges of the graph
            
            for i in range(len(nodes)): # For each node in the graph (the number of nodes is the same as the number of rows and columns in the adjacency matrix) 
                for j in range(len(AdjacentMatrix[i])): # For each connection of the node (the number of connections is the same as the number of rows and columns in the adjacency matrix)
                    if AdjacentMatrix[i][j] == 1: # If the connection exists (the value in the adjacency matrix is 1) 
                        g.addEdge(nodes[i], nodes[j]) # Add the edge to the graph (the edge is between the node and the connection)


            print(f"DFS on Graph { graphNumber }:")
            visited = defaultdict(lambda: "white") # white - not visited, gray - visited, black - finished visiting all the nodes connected to it  
            g.DFS(str(startingNode), visited, None, 0) # DFS algorithm starting from the first node in the graph (0) and None as parent and level 0 
            print(f"None\nBFS on Graph {graphNumber}:")
            g.BFS(str(startingNode)) # BFS algorithm starting from the first node in the graph (0
            count = 1
            startingNode = None

def DFSandBFSonIncidentMatrix():
    with open('Incidence_Matrix.txt', 'r') as f:
        # Read the number of graphs
        num_graphs = int(f.readline().strip())
        for i in range(num_graphs):
            graphNumber = i + 1
            g = Graph()
            # Read the nodes and incidence matrix
            nodes = [] # Create an empty list to store the nodes of the graph in (the nodes are the first line of the graph)
            inc_matrix = [] # Create an empty list to store the incidence matrix of the graph in (the incidence matrix is the second line of the graph)
            line = f.readline().strip() # Read the first line of the graph and strip the newline character from the end of the line (if there is one)
            count = 1
            startingNode = None
            while line != '*********': # While the line is not the end of the graph
                node, connections = line.split('\t') # Split the line into the node and the connections (the connections are separated by a tab character)
                if count == 1:
                    startingNode = node
                    count += 1
                connections = connections.replace('(','').replace(')','') # Remove the parentheses from the connections
                nodes.append(node) # 
                inc_matrix.append([int(x) for x in connections.strip().split(',') if x != ''])
                line = f.readline().strip()

            # Print the edges of the graph
            for i in range(len(nodes)):
                for j in range(len(inc_matrix)):
                    for k in range(len(inc_matrix)):
                        if inc_matrix[i][j] == 1 and inc_matrix[k][j] == -1:
                            find = True
                            g.addEdge(nodes[i], nodes[k])
                            
                if find == False:
                    g.addEdge(nodes[i], nodes[i])
                find = False
            
            print(f"DFS on Graph { graphNumber }:")
            visited = defaultdict(lambda: "white") # white - not visited, gray - visited, black - finished visiting all the nodes connected to it  
            g.DFS(str(startingNode), visited, None, 0) # DFS algorithm starting from the first node in the graph (0) and None as parent and level 0 
            print(f"None\nBFS on Graph {graphNumber}:")
            g.BFS(str(startingNode)) # BFS algorithm starting from the first node in the graph (0
            count = 1
            startingNode = None              
        

print("On Which Graph Do You Want To Perform DFS and BFS?")
print("1. Adjacency List")
print("2. Adjacency Matrix")
print("3. Incident Matrix")

choice = int(input("Enter Your Choice: "))

if choice == 1:
    DFSandBFSOnAdjacentList()
elif choice == 2:
    DFSandBFSOnAdjacentMatrix()
elif choice == 3:
    DFSandBFSonIncidentMatrix()
else:
    print("Invalid Choice")





