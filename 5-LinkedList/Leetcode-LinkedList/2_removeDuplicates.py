def removeDuplicates(head):

    current = head

    while current:
        while current.next and current.val == current.next.val:
            current.next = current.next.next
        current = current.next
        
    return head