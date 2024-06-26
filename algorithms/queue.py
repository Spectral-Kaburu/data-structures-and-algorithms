from collections import deque
import threading
import time
import math


def binary(val):
    global prev, nest
    count = 0
    for _ in range(32):
        prev = eval(str(2 ** (count - 1)))
        nest = eval(str(2 ** count))
        if type(prev) == float:
            prev = math.ceil(prev)
        if val in range(prev, nest):
            break
        elif val == nest:
            ans = ''
            ans += '1'
            ans += '0' * count
            return ans
        else:
            count += 1

    """while len(ans) < (count + 1):
        counter = 0
        if"""
    print(prev, nest, count)


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        return self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def order(self, orders):
        place = []

        def place_order(orders):
            for order in orders:
                place.insert(0, order)
                time.sleep(0.5)

        def serve_order(server):
            for _ in range(len(orders)):
                print(server[-1])
                server.pop()
                time.sleep(2)

        take = threading.Thread(target=place_order, args=(orders,))
        take.start()
        serve = threading.Thread(target=serve_order, args=(place,))
        time.sleep(1)
        serve.start()


q = Queue()
print(binary(16))
