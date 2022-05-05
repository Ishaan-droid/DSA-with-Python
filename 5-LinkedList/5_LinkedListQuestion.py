from random import randint

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(node.val) for node in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        current = self.head

        while current:
            result += 1
            current = current.next
        
        return result

    def append(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return self.tail

    def generate(self,n,min_value,max_value):
        self.head = None
        self.tail = None
        
        for i in range(n):
            self.append(randint(min_value,max_value))

        return self

    def removeDuplicates(self):
        current = self.head
        print(self)
        # arr = []

        obj = {}

        while current.next:
            if current.next.val not in obj:
                obj[current.val] = 1
            else:
                current.next = current.next.next
                
            current = current.next


        # while current:
        #     arr.append(current.val)
        #     current = current.next
        
        # obj = {}

        # for a in arr:
        #     if a not in obj:
        #         obj[a] = 1
        #     else:
        #         continue
        
        # self.head = None
        # self.tail = None

        # for i in list(obj.keys()):
        #     self.append(i)

        return self


customLinkedList = LinkedList()
customLinkedList.generate(10,0,5)

x = customLinkedList.removeDuplicates()
print(x)
            