def removeNthFromLast(n,head):
    length = 0
    current = head

    while current:
        current = current.next
        length += 1

    if n > length:
        return None
        
    current = head
        
    if n == length:
        current = current.next
        return current
        
    findIndex = length - n
    index = 0

    while current.next:
        if index == findIndex-1:
            current.next = current.next.next
            return head
        else:
            index += 1
            
        current = current.next