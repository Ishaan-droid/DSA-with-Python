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

        print(self)
        return self

    def removeDuplicates(self):
        # Solution 1 (Leetcode)

        # current = head

        # while current:
        #     while current.next and current.val == current.next.val:
        #         current.next = current.next.next
        #     current = current.next
        
        # return head

        # Solution 2

        current = self.head
        mySet = set([current.val])

        while current.next:
            if current.next.val in mySet:
                current.next = current.next.next
            else:
                mySet.add(current.next.val)
                current = current.next
        
        return self

    def findNthFromLastElement(self, loc):
        pointer1 = self.head
        pointer2 = self.head

        for i in range(loc):
            pointer2 = pointer2.next

        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1


customLinkedList = LinkedList()
customLinkedList.generate(5,0,5)

# x = customLinkedList.removeDuplicates()
# x = customLinkedList.NthFromLastElement(2)
x = customLinkedList.findNthFromLastElement(4)
print(x)
            