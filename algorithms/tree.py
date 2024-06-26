class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = " " * self.get_level()
        prefix = spaces + '|__'
        print(self.data)
        if self.children:
            for child in self.children:
                print(prefix+child.data)


def build_tree():
    stem = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("mac"))
    laptop.add_child(TreeNode("think_pad"))
    laptop.add_child(TreeNode("hp"))

    cell_phone = TreeNode("Cell_phone")
    cell_phone.add_child(TreeNode("iphone"))
    cell_phone.add_child(TreeNode("Techno"))
    cell_phone.add_child(TreeNode("Huawei"))

    tv = TreeNode("Television")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Hi_sense"))
    tv.add_child(TreeNode("LG"))

    stem.add_child(laptop)
    stem.add_child(cell_phone)
    stem.add_child(tv)

    return stem


if __name__ == "__main__":
    root = build_tree()
    root.print_tree()
    # print(root.get_level())
    pass
