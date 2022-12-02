from collections import deque

#Making a class to make a treeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    #Level Order Traversal of the graph using BFS
    def levelOrder(self):
        #Edge case: Check if the tree is NULL, then just return empty list cause you have nothing
        if self is None:
            return []
        
        #BFS uses Queue, add the initial starting node to the queue and the levels will be stored in the
        # result var which is our output
        result = []

        queue = deque([])
        queue.append(self)

        #Iterate through the queue which will contain the level-wise nodes
        while queue:
            #Create an array to contain the level nodes
            level = []
            for i in range(len(queue)):
                #Take the first node in the queue (waited patiently for it's turn bruh, gotta respect)
                currentNode = queue.popleft()
                #Add that node to the current level array
                level.append(currentNode.val)
                #Now if the left and the right nodes exist for this node, then you just add them to the queue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:    
                    queue.append(currentNode.right)
            
            #Add the level generated to the result list 
            if level:
                result.append(level)
        
        #Once iterated through the entire tree, queue will end, then just return the list
        return result

#Just some code to try this out
#Tree which is made is like this
'''
        3
       / \
      9  20
        /  \
       15   7
'''
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

levelOrder = tree.levelOrder()
print(levelOrder)


