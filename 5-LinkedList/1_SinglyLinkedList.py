from pprint import pprint

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SinglyLinkedList:
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

            while index < loc-1: # -1 because we will traverse to the node before which we need to delete
                current = current.next
                index += 1

            tempNode = current.next
            current.next = newNode
            newNode.next = tempNode

            if current == self.tail : self.tail = newNode

    def traverse(self):
        if self.head is None:
            return print('The single linked list does not exist.')
        else:
            current = self.head
            while current:
                print(current.val)
                current = current.next

    def search(self,loc):
        if self.head is None:
            return print('The singly linked list does not exist.')
        else:
            index = 0
            current = self.head

            while current:
                if index == loc:
                    return print('We have found the node.',current.val)
                current = current.next
                index += 1

            return print('The index is out of bounds.')

    def pop(self,loc=-1):
        if self.head is None:
            return print('The single linked list does not exist.')
        elif loc == 0:
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif loc == -1:
            current = self.head

            if current.next is None:
                current = None
            else: 
                while current:
                    if current.next == self.tail:
                        self.tail = current
                        self.tail.next = None
                        return True
                    current = current.next
        else:
            index = 0
            current = self.head

            while index < loc-1: # -1 because we will traverse to the node before which we need to delete
                current = current.next
                index += 1

            newNode = current.next.next
            current.next = newNode
            
    def clear(self):
        self.head = None
        self.tail = None

linkedList = SinglyLinkedList()

linkedList.append(5)
linkedList.append(10)
linkedList.append(15)
linkedList.append(20)
linkedList.append(25)
# linkedList.insert(2,35)
# linkedList.insert(4,40)

# linkedList.traverse()
# linkedList.search(2)
# linkedList.pop(2)
# linkedList.clear()

for node in linkedList:
    # pprint(vars(node))
    print(node.val)






