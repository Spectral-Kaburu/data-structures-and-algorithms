class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Linked_List:
    def __init__(self):
        self.head = None

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def get_element(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index.")

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                return itr
            count += 1
            itr = itr.next

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, self.head, None)
            return

        self.head = Node(data, self.head, None)
        itr = self.head
        count = 0
        while itr:
            its = self.get_element(count)
            if its:
                itr.prev = its
            count += 1
            itr = itr.next

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index.")

        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == (self.get_length() - 1):
            self.insert_at_end(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next, itr)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_set):
        for data in data_set:
            self.insert_at_end(data)

    def remove_by_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index.")

        itr = self.head
        count = 0

        if index == 0:
            itr = itr.next
            return 

        while itr:
            if count == index:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def reverse_print(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index.")
        itr = self.head
        llstr = ''
        count = 0

        if index == 0:
            llstr = "-" + str(itr.data) + "-"
            print(llstr)
            return

        while itr:
            if count == index:
                while itr:
                    llstr += '<--' + str(itr.data)
                    itr = itr.prev
                break
            itr = itr.next
            count += 1

        print(llstr)

    def print(self):
        itr = self.head
        llstr = ''

        while itr:
            llstr += '-->' + str(itr.data) + '-'
            itr = itr.next

        print(llstr)

    def forward_print(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        itr = self.head
        llstr = ''
        count = 0

        while itr:
            if count == index + 1:
                while itr:
                    llstr += '-->' + str(itr.data) + '-'
                    itr = itr.next
                break
            itr = itr.next
            count += 1

        print(llstr)


if __name__ == "__main__":
    ll = Linked_List()
    """ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.reverse_print(2)
    ll.forward_print(2)"""
    ll.insert_values(["mango", "orange", "apple", "grapes"])
    ll.insert_at(2, "avocado")
    ll.remove_by_index(0)
    ll.print()
