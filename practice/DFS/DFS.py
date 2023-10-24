from collections import defaultdict

#Making a graph which is like a dict containing a list
#key = node, value = list [] containing the neighbours of the node
graph = defaultdict(list)

#Function to add the edges to the neighbors
def addEdge(graph, u, v):
    graph[u].append(v)



def DFS(node):

    #Create a visited list which stores all the visited nodes initially
    #Initially all the nodes are unvisited so keep them as False
    visited = [False] * (max(graph) + 1)

    #DFS (iterative) uses Stack, hence add the initial starting node to the stack and mark it as visited 
    stack = []
    stack.append(node)

    while(len(stack)):
        #Get the node which is at the top of the stack
        currentNode = stack[-1]
        stack.pop()

        #Check if the node is not visited, if so, then print it out
        if not visited[currentNode]:
            print(currentNode, end=' ')
            visited[currentNode] = True
        
        #Find the neighbours of the node and then add them to the stack if they aren't visited
        for neighbour in graph[currentNode]:
            if not visited[neighbour]:
                stack.append(neighbour)


#Creating the graphs, the graphs is like this
'''
    0 - 1
    | /  
    2 - 3 ]  
'''
addEdge(graph, 0, 1)
addEdge(graph, 0, 2)
addEdge(graph, 1, 2)
addEdge(graph, 2, 0)
addEdge(graph, 2, 3)
addEdge(graph, 3, 3)

print("Depth First Search of the Graph is: - ")
DFS(0)