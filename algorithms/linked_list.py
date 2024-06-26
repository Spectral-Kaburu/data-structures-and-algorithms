class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("The linked list is empty!!!")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0

        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_by_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        itr = self.head

        if index == 0:
            self.head = itr.next
            return

        count = 0
        while count < index - 1:
            count += 1
            itr = itr.next
        itr.next = itr.next.next

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == self.get_length():
            self.insert_at_end(data)
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        count = 0

        while itr:
            if itr.data == data_after:
                self.insert_at(count + 1, data_to_insert)
                return
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        itr = self.head
        count = 0

        while itr:
            if itr.data == data:
                self.remove_by_index(count)
                return
            count += 1
            itr = itr.next
        raise ValueError("Invalid data.")


if __name__ == "__main__":
    ll = Linked_List()
    """ll.insert_at_beginning(567)
    ll.insert_at_beginning(354)
    ll.insert_at_beginning(213)
    ll.insert_at_beginning(633)
    ll.insert_at_beginning(3333)
    ll.insert_at_end(647)
    ll.insert_at_end(836)
    ll.insert_at_end(142)"""
    ll.insert_values(["banana", "mango", "apple", "grapes"])
    ll.insert_at(3, "orange")
    ll.insert_after_value("apple", "jackfruit")
    ll.print()
