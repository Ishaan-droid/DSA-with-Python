class Node:
    def __init__(self,val):
        self.val = val;
        self.next = None;

class singlyLinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;
        self.length = 0;

linkedList = singlyLinkedList()
node1 = Node(4)
node2 = Node(5)

linkedList.head = node1
linkedList.head.next = node2
linkedList.tail = node2

print(node1.next)

