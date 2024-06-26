class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return

        if data > self.data:
            if self.right:
                self.right.add_child(data)

            else:
                self.right = BinaryTree(data)

        if data < self.data:
            if self.left:
                self.left.add_child(data)

            else:
                self.left = BinaryTree(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    """def post_order_traversal(self):
        elements = []
        
        return elements"""

    def calculate_sum(self):
        try:
            ans = sum(self.in_order_traversal())
            return ans
        except TypeError as e:
            return e

        except Exception as e:
            return e

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)

            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)

            else:
                return False

    def delete(self, val):
        s = self
        if val < s.data:
            if self.left:
                self.left = self.left.delete(val)

        if val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete(min_val)

        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()


def build_tree(data):
    root = BinaryTree(data[0])

    for i in range(1, len(data)):
        root.add_child(data[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    countries = ["India", "Kenya", "USA", "Russia", "Georgia", "Kenya", "Uganda"]
    countries_tree = build_tree(countries)
    numbers_tree = build_tree(numbers)
    # print(countries_tree.calculate_sum())
    numbers_tree.delete(88)
    print(numbers_tree.in_order_traversal())
