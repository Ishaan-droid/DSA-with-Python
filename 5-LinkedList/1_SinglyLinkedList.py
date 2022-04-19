from pprint import pprint

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while(node):
            yield node
            node=node.next
    def append(self,val):
        newNode = Node(val)

        if self.head == None:
            self.head = newNode
            self.tail = newNode

        self.tail.next = newNode
        self.tail = newNode
        newNode.next = None
    def insert(self,loc,val):
        newNode = Node(val)

        if loc == 0:
            temp = self.head
            self.head = newNode
            newNode.next = temp
        else:
            current = self.head
            index = 0

            while index < loc-1:
                current = current.next
                index += 1

            tempNode = current.next
            current.next = newNode
            newNode.next = tempNode

            if current == self.tail : self.tail = newNode


linkedList = singlyLinkedList()

linkedList.append(5)
linkedList.append(10)
linkedList.append(15)
linkedList.append(20)
linkedList.insert(2,35)
linkedList.insert(4,40)

for node in linkedList:
    # pprint(vars(node))
    print(node.val)






