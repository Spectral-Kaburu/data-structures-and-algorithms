class Hash_Table:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        count = 0

        for char in key:
            count += ord(char)

        return count % self.MAX

    def __setitem__(self, key, value):
        count = self.get_hash(key)
        self.arr[count] = value


ht = Hash_Table()
ht.__setitem__("oranges", 20)
ht.__setitem__("mangoes", 13)
ht.__setitem__("apples", 35)
