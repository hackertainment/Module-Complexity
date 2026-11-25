from dataclasses import dataclass

@dataclass
class Node:
    char = None  # character string
    next = None  # <__main__.Node object>
    prev = None  # <__main__.Node object>

class LinkedList:
    def __init__(self):
        self.head = None  # <__main__.Node object>
        self.tail = None  # <__main__.Node object>

    def __str__(self):
        forwards = ["HEAD"]
        traverse = self.head
        while (traverse is not None):
            forwards.append(traverse.char)
            traverse = traverse.next
        backwards = ["TAIL"]
        traverse = self.tail
        while (traverse is not None):
            backwards.insert(0, traverse.char)
            traverse = traverse.prev
        return ("  -> ".join(forwards))+"  -> None\nNone <-  "+(" <-  ".join(backwards))
        
    def push_head(self, char):
        node = Node()
        node.char = char
        if (self.head is not None):
            node.next = self.head
            self.head.prev = node
        self.head = node
        if (self.tail is None):
            self.tail = node
        return node

    def pop_tail(self):
        tail = self.tail
        self.remove(self.tail)
        return tail.char if tail else None

    def remove(self, node):
        if (node is not None):
            if (node.next is not None):
                node.next.prev = node.prev
            if (node.prev is not None):
                node.prev.next = node.next
            if (self.head is node):
                self.head = node.next
            if (self.tail is node):
                self.tail = node.prev


if __name__ == "__main__":
    print(LinkedList())
