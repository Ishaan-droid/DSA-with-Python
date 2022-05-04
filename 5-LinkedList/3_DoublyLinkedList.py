from pprint import pprint

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next
    
    def createDoublyLinkedList(self,val):
        newNode = Node(val)

        # newNode.next = None
        newNode.prev = None
        self.head = newNode
        self.tail = newNode

        return print('Doubly Linked List is created successfully.')

    def append(self,val):
        if self.head is None:
            return print('Create doubly linked list first.')

        newNode = Node(val)

        newNode.next = None
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def insert(self,loc,val):
        if self.head is None:
            return print('Create doubly linked list first.')

        newNode = Node(val)

        if loc == 0:
            temp = self.head
            self.head.prev = newNode
            newNode.next = temp
            self.head = newNode
        else:
            current = self.head
            index = 0

            while index < loc -1:
                current = current.next
                index += 1

            temp = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = temp

    def traverse(self):
        if self.head is None: return print('Linked list not created')

        current = self.head

        while current:
            print(current.val)
            current = current.next

    def reverseTraverse(self):
        if self.head is None: return print('Linked list not created')

        current = self.tail

        while current:
            print(current.val)
            current = current.prev

    def search(self,loc):
        current = self.head
        index = 0

        while current:
            if index == loc:
                return print('Node found',current.val)

            current = current.next
            index += 1
        
        return print('Index is out of bounds')

    def pop(self):
        newTail = self.tail.prev
        self.tail = newTail
        self.tail.next = None

    def deleteNode(self,loc=0):
        if loc == 0:
            tempNode = self.head.next
            self.head = tempNode
            self.head.prev = None
        else:
            current = self.head
            index = 0

            while index < loc - 1:
                current = current.next
                index += 1

            temp = current.next
            current.next = current.next.next
            current.next.prev = temp

    def deleteEntireList(self):
        self.head = None
        self.tail = None




linkedList = DoublyLinkedList()

linkedList.createDoublyLinkedList(5)
linkedList.append(10)
linkedList.append(15)
linkedList.append(20)
linkedList.append(25)
linkedList.append(30)

# linkedList.insert(2,25)
# linkedList.insert(0,0)
# linkedList.traverse()
# linkedList.reverseTraverse() 
# linkedList.search(1)
# linkedList.pop()
# linkedList.deleteNode(3)
# linkedList.deleteEntireList()

for node in linkedList:
    pprint(vars(node))
    # print(node.val)
        
