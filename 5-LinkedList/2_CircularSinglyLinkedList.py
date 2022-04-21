from pprint import pprint

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def create(self,val):
        newNode = Node(val)
        self.head = newNode
        self.tail = newNode
        self.tail.next = self.head
        return print('Circular linked list created')

    def append(self,val):
        if self.head is None:
            return print('Create the circular linked list first.')

        newNode = Node(val)

        self.tail.next = newNode
        self.tail = newNode
        newNode.next = self.head

    def insert(self,loc,val):
        if self.head is None:
            return print('Create the circular linked list first.')
        
        newNode = Node(val)

        if loc == 0:
            temp = self.head
            self.head = newNode
            newNode.next = temp
            self.tail.next = self.head
        else:
            index = 0
            current = self.head

            while index < loc - 1:
                current = current.next
                index += 1

            temp = current.next
            current.next = newNode
            newNode.next = temp

    def traverse(self):
        current = self.head

        while current:
            print(current,current.val)
            current = current.next

            if self.tail.next == current:
                break


linkedList = CircularSinglyLinkedList()

linkedList.create(5)
linkedList.append(10)
linkedList.append(15)
linkedList.append(20)
linkedList.insert(2,45)

linkedList.traverse()

# for node in linkedList:
#     print(node.val)
    # pprint(vars(node))
