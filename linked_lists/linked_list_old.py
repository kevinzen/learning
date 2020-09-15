
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):

    def __init__(self, head = None):
        self.head = head

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def size(self):
        count = 0
        if not self.head:
            return count
        node = self.head
        while node:
            count = count + 1
            node = node.next
        return count

    def search(self, data):
        if not self.head:
            return False
        node = self.head

        while node:
            if node.data == data:
                return True
            node = node.next

        return False

    def delete(self, data):
        if not self.head:
            return False

        prev_node = None
        node = self.head
        while node:
            if node.data == data:
                if prev_node:
                    prev_node.next = node.next
                else:
                    self.head = node.next
                return True
            else:
                prev_node = node
                node = node.next
        return False



