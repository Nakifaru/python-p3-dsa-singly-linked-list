class Node:
    
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, node):
        if self.head == None:
            self.head = node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = node


bulldog = Node("Bulldog")
chihuaha = Node("Chihuahua")
bulldog.next_node = chihuaha
german_shephard = Node("German Shephard")
chihuaha.next_node = german_shephard


list = LinkedList()
list.append(Node("Bulldog"))