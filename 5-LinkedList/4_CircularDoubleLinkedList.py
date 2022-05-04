from pprint import pprint

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next

            if current == self.tail.next:
                break

    def createCircularDoubleLinkedList(self,val):
        newNode = Node(val)

        if self.head is not None:
            return print('Circular Double Linked List already created')

        self.head = newNode
        self.tail = newNode
        self.tail.next = self.head
        self.head.prev = self.tail

        return print('The Circular Double Linked List is created.')

    def insert(self,val,loc=0):
        if self.head is None:
            return print('Please create the Circular Double Linked List.')

        newNode = Node(val)

        if loc == 0:
            temp = self.head
            self.head = newNode
            self.head.next = temp
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            current = self.head
            index = 0

            while index < loc - 1:
                current = current.next
                index += 1

            temp = current.next
            current.next = newNode
            newNode.next = temp
            newNode.prev = current

    def append(self,val):
        newNode = Node(val)

        newNode.next = self.head
        newNode.prev = self.tail
        self.head.prev = newNode
        self.tail.next = newNode
        self.tail = newNode
        


linkedList = CircularDoubleLinkedList()

linkedList.createCircularDoubleLinkedList(5)
linkedList.append(10)
linkedList.append(15)
linkedList.append(20)
linkedList.insert(25,2) 

for node in linkedList:
    pprint(vars(node))
    # print(node.val)