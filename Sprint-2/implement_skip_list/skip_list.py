import math
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
        dummy = Node()
        dummy.key = -math.inf
        self.heads = [dummy]  # array of <__main__.Node object>
        '''
        p = None
        dummy = Node()
        dummy.key = -math.inf
        dummy.below = self.heads[0]
        self.heads[0].above = dummy
        self.heads.append(dummy)
        q = None
        dummy = Node()
        dummy.key = -math.inf
        dummy.below = self.heads[1]
        self.heads[1].above = dummy
        self.heads.append(dummy)
        r = None
        for i in range(70, 0, -10):
            node = Node()
            node.key = i
            node.next = p
            if (p is not None):
                p.prev = node
            p = node
            if (p.key==10 or p.key==30 or p.key==50 or p.key==70):
                node = Node()
                node.key = i
                node.next = q
                node.below = p
                p.above = node
                if (q is not None):
                    q.prev = node
                q = node
            if (p.key==30 or p.key==50):
                node = Node()
                node.key = i
                node.next = r
                node.below = q
                q.above = node
                if (r is not None):
                    r.prev = node
                r = node
        self.heads[0].next = p
        self.heads[1].next = q
        self.heads[2].next = r
        '''

    def __str__(self):
        levels = []
        for i in range(0, len(self.heads)):
            levels.append("None <- HEAD["+str(i)+"]:"+str(self.heads[i].key))
            p = self.heads[i].next
            while (p is not None):
                padding = "="*(levels[0].find("<=> "+str(p.key)+" ")-len(levels[i])) if i>0 else "="
                levels[i] = levels[i]+" <"+padding+"> "+str(p.key)
                p = p.next
            padding = "-"*(levels[0].find("-> None")-len(levels[i])) if i>0 else "-"
            levels[i] = levels[i]+" "+padding+"> None"
        return ("\n".join(reversed(levels)))

    def __contains__(self, key):
        return (key==(self.search(key).key))

    def to_list(self):
        keys = []
        p = self.heads[0].next
        while (p is not None):
            keys.append(p.key)
            p = p.next
        return keys

    def search(self, key):
        level = len(self.heads)-1
        p = self.heads[level]
        while ((p.below is not None) or ((p.next is not None) and (key>=p.next.key))):  # while (not reaching bottom level) or (can still move right)
            #print(p.key, end=" ")
            if ((p.next is not None) and (key>=p.next.key)):  # if (next key is not INFINITY) and (k >= next key)
                p = p.next                                    # then go next one right
                #print(">", end=" ")
            else:                                             # else go down one level
                if (p.below is not None):
                    p = p.below
                    #print("v", end=" ")
        #print()
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
                if (self.heads[i-1].next is not None):
                    node = Node()
                    node.key = self.heads[i-1].key
                    node.left
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


if __name__ == "__main__":
    print(SkipList())
    print(SkipList().to_list())
    '''
    print()
    sl = SkipList()
    print(sl.to_list())
    print(sl)
    for i in range(5, 80, 5):
        p = sl.search(i)
        print("search", "key="+str(i), "found", "p="+str(p.key))
    '''
    #print()
    #sl = SkipList()
    #sl.insert(30)  # insert into empty list
    #sl.insert(70)  # insert at tail
    #sl.insert(50)  # insert at middle
    #sl.insert(10)  # insert at head
