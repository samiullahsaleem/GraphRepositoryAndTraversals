def printGraphsFromAdjacentList():
    try:
        with open('Adjacency_list.txt', 'r') as f:
            numberOfGraphs = int(f.readline().strip())
            for i in range(numberOfGraphs):
                nodes = []
                connections = []
                line = f.readline().strip()# Read the first line of the graph and strip the newline character from the end of the line (if there is one)
                print("Graph", i+1)
                try: 
                    while line != '*********' :
                        try:
                            node, connections = line.split('\t')
                        except:
                            node = line
                            connections = 'None' 
                        nodes.append(node)
                        connections = connections.replace(' ','')
                        connections=connections.split(',')
                        
                        for i in range(len(connections)):
                            print(f"{node} -> {connections[i]}")
                        line = f.readline().strip()
                except:
                    print("An Exception occur from your side. Please check your file and try again")
    except FileNotFoundError:
        print("File not found")

def printGraphsFromAdjacentMatrix():
    try:
        with open('Adjacency_Matrix.txt', 'r') as f: # Open the file for reading
            # Read the number of graphs
            num_graphs = int(f.readline().strip()) # Read the first line and convert it to an integer (the number of graphs) and strip the newline character from the end of the line (if there is one)
            for i in range(num_graphs): # For each graph in the file (the number of graphs is given in the first line of the file) 
                # Read the nodes and adjacency matrix
                nodes = [] # Create an empty list to store the nodes of the graph in (the nodes are the first line of the graph) 
                AdjacentMatrix = [] # Create an empty list to store the adjacency matrix of the graph in (the adjacency matrix is the second line of the graph) 
                line = f.readline().strip() # Read the first line of the graph and strip the newline character from the end of the line (if there is one)
                while line != '*********':
                    node,connections = line.split('\t') # Split the line into the node and the connections (the connections are separated by a tab character)
                    nodes.append(node) # Add the node to the list of nodes of the graph 
                    AdjacentMatrix.append([int(x) for x in connections.split(',')]) # Add the connections to the adjacency matrix of the graph (the connections are separated by a comma character)
                    line = f.readline().strip() # Read the next line of the graph and strip the newline character from the end of the line (if there is one)
                # Print the edges of the graph
                print("Graph", i+1)
                for i in range(len(nodes)): # For each node in the graph (the number of nodes is the same as the number of rows and columns in the adjacency matrix) 
                    for j in range(len(AdjacentMatrix[i])): # For each connection of the node (the number of connections is the same as the number of rows and columns in the adjacency matrix)
                        if AdjacentMatrix[i][j] == 1: # If the connection exists (the value in the adjacency matrix is 1) 
                            print(f"{nodes[i]} -> {nodes[j]}") # Print the edge (the edge is the node and the connection separated by an arrow) 
    except FileNotFoundError:
        print("File not found")

find = False
def printGraphFromIncidenceMatrix():
    with open('Incidence_Matrix.txt', 'r') as f:
        # Read the number of graphs
        num_graphs = int(f.readline().strip())
        for i in range(num_graphs):
            # Read the nodes and incidence matrix
            nodes = [] # Create an empty list to store the nodes of the graph in (the nodes are the first line of the graph)
            inc_matrix = [] # Create an empty list to store the incidence matrix of the graph in (the incidence matrix is the second line of the graph)
            line = f.readline().strip() # Read the first line of the graph and strip the newline character from the end of the line (if there is one)
            while line != '*********': # While the line is not the end of the graph
                node, connections = line.split('\t') # Split the line into the node and the connections (the connections are separated by a tab character)
                connections = connections.replace('(','').replace(')','') # Remove the parentheses from the connections
                nodes.append(node) # 
                inc_matrix.append([int(x) for x in connections.strip().split(',') if x != ''])
                line = f.readline().strip()

            print("Graph", i+1)
            # Print the edges of the graph
            for i in range(len(nodes)):
                for j in range(len(inc_matrix)):
                    for k in range(len(nodes)):
                        if inc_matrix[i][j] == 1 and inc_matrix[k][j] == -1:
                            print(f"{nodes[i]} -> {nodes[k]}") 
                            find = True                            
                if find == False:
                    print(f"{nodes[i]} -> {nodes[i]}")
                find = False

print("What do you want to do? \n 1. Print graphs from Adjacency List \n 2. Print graphs from Adjacency Matrix \n 3. Print graphs from Incidence Matrix")
choice = int(input("Enter your choice: "))
if choice == 1:
    printGraphsFromAdjacentList()
elif choice == 2:
    printGraphsFromAdjacentMatrix()
elif choice == 3:
    printGraphFromIncidenceMatrix()
