from collections import deque, defaultdict

#Making a graph which is like a dict containing a list
#key = node, value = list [] containing the neighbours of the node
graph = defaultdict(list)

#Function to add the edges to the neighbors
def addEdge(graph, u, v):
    graph[u].append(v)



def BFS(node):

    #Create a visited list which stores all the visited nodes initially
    #Initially all the nodes are unvisited so keep them as False
    visited = [False] * (max(graph) + 1)

    #BFS uses Queue, add the initial starting node to the queue and mark it as visited 
    queue = deque([])
    queue.append(node)
    visited[node] = True


    while queue:
        #Get the node which is at the start of the queue, print it, and we explore that
        currentNode = queue.popleft()
        print(currentNode, end=" ")

        #Explore = check each neighbours for that node
        for neighbour in graph[currentNode]:
            #If the node is not visited, add it to the end of queue and mark it as visited
            if visited[neighbour] == False:
                queue.append(neighbour)
                visited[neighbour] = True


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

print("Breadth First Search of the Graph is: - ")
BFS(0)