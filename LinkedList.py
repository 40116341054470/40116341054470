class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        t = self.head
        while t:
            print(t.data, end=' --> ')
            t = t.next
        print('None')

    def add_in_start(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def add_in_end(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
        else:
            t = self.head
            while t.next:
                t = t.next
            t.next = n

    def add_after(self, m, d):
        n = Node(d)
        t = self.head
        while t and t.data != m:
            t = t.next
        if t:
            n.next = t.next
            t.next = n

    def del_first(self):
        if self.head:
            self.head = self.head.next
        else:
            return 'empty'

    def del_last(self):
        if self.head and self.head.next:
            t = self.head
            while t.next.next:
                t = t.next
            t.next = None

    def del_after(self, m):
        t = self.head
        while t and t.data != m:
            t = t.next
        if t and t.next:
            t.next = t.next.next