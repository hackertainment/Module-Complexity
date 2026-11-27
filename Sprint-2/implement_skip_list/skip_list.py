import random
from dataclasses import dataclass

@dataclass
class Node:
    key = None
    prev = None  # <__main__.Node object>
    next = None  # <__main__.Node object>
    above = None  # <__main__.Node object>
    below = None  # <__main__.Node object>

# https://brilliant.org/wiki/skip-lists/
# https://upload.wikimedia.org/wikipedia/commons/8/86/Skip_list.svg
class SkipList:
    def __init__(self):
        self.heads = [Node()]  # array of <__main__.Node object> with dummy head node

    def __str__(self):
        levels = []
        for i in range(0, len(self.heads)):
            levels.append("None <- HEAD["+str(i)+"]DUMMY")
            p = self.heads[i].next
            while (p is not None):
                levels[i] = levels[i]+" <=> "+str(p.key)
                p = p.next
            levels[i] = levels[i]+" -> None"
        return ("\n".join(reversed(levels)))

    #def __contains__(self, key):
    #    pass

    def to_list(self):
        keys = []
        if (len(self.heads)>0):
            p = self.heads[0].next
            while (p is not None):
                keys.append(p.key)
                p = p.next
        return keys

    """
    Search(key)
        p = top-left node in S
        while (p.below != null) do        //Scan down
            p = p.below
            while (key >= p.next) do      //Scan forward
                p = p.next
        return p
    """
    def search(self, key):
        level = len(self.heads)-1
        p = self.heads[level]
        while (p.below is not None):
            p = p.below
            while ((p.next is not None) and (key>=p.next.key)):
                p = p.next
        return p

    """
    Insert(key)
        p = Search(key)
        q = null
        i = 1
        repeat
            i = i + 1                   //Height of tower for new element
            if i >= h
                h = h + 1
                createNewLevel()        //Creates new linked list level
            while (p.above == null)
                p = p.prev              //Scan backwards until you can go up
            p = p.above
            q = insertAfter(key, p)     //Insert our key after position p
        until CoinFlip() == 'Tails'
        n = n + 1
        return q
    """
    def insert(self, key):
        p = self.search(key)
        q = None
        i = 0
        coinflip = True
        while coinflip:
            i = i+1
            if (i>=len(self.heads)):
                dummy = Node()
                self.heads.append(dummy)
                dummy.below = self.heads[i-1]
                self.heads[i-1].above = dummy
            #while (p.above is None):
            #    p = p.prev
            #p = p.above
            node = Node()
            node.key = key
            node.prev = p
            if (p is not None):
                node.next = p.next
            if (node.next is not None):
                node.next.prev = node
            if (node.prev is not None):
                node.prev.next = node
            else:
                self.heads[i] = node
            q = node
            coinflip = False #bool(random.randint(0, 1))

    """
    Delete(key)
    Search for all positions p_0, ..., p_i where key exists
    if none are found
        return
    Delete all positions p_0, ..., p_i
    Remove all empty layers of skip list
    """
    def delete(self, key):
        pass

    '''
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
    '''


if __name__ == "__main__":
    print(SkipList())
    print(SkipList().to_list())
    print()
    sl = SkipList()
    sl.insert(50)  # insert into empty list
    sl.insert(90)  # insert at tail
    sl.insert(70)  # insert at middle
    sl.insert(30)  # insert at head
    print(sl.to_list())
    print(sl)
