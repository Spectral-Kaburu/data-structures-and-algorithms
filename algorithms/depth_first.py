class BinaryTree():
    def __init__(self, data:int):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data:list[int]):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.insert(data)
            
            else:
                self.left = BinaryTree(data)

        if data > self.data:
            if self.right:
                self.right.insert(data)
            
            else:
                self.right = BinaryTree(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements

    def depth_first_search(self, val:int):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.depth_first_search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.depth_first_search(val)
            else:
                return False


def build_tree(data:list[int]):
    root = BinaryTree(data[0])
    for i in range(1, len(data)):
        root.insert(data[i])
    
    return root


if __name__ == "__main__":
    numbers = [17, 15, 13, 19, 23, 33 ,59]
    tree = build_tree(numbers)
    print(tree.in_order_traversal())
    print(tree.depth_first_search(23))



