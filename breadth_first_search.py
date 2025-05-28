class BreadthFirst():
    def __init__(self, data:int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data:list[int]):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BreadthFirst(data)
            
        if data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BreadthFirst(data)

    def print(self):
        elements = []
        
        elements.append(self.data)

        if self.left:
            elements += self.left.print()

        if self.right:
            elements += self.right.print()
        
        return elements

    def getto(self, val:int):
        if val == self.data:
            return self.data
        if val < self.data:
            if self.left:
                return self.left.getto(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.getto(val)
            else:
                return False
    
    def bfs(self, val: int):
    # Initialize a queue for BFS, starting with the root node (self)
        queue = [self]
        
        while queue:
            current_node = queue.pop(0)  # Pop the first node from the queue
            
            # Check if the current node's data matches the value
            if current_node.data == val:
                return current_node.data
            
            # Add left and right children to the queue if they exist
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        # If the value was not found
        return False


        

def build_tree(data:list[int]):
    root = BreadthFirst(data[0])

    for i in range(1, len(data)):
        root.insert(data[i])

    return root

numbers = [5, 3, 0, 1, 7, 3, 9, 6, 4, 9, 2, 7]
root = build_tree(numbers)


print(root.bfs(7))