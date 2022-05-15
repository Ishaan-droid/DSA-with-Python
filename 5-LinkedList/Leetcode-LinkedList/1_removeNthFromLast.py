def removeNthFromLast(n,head):
    pass
    # Solution 2 (Leetcode)

    # dummy = ListNode(0,head)
    # pointer1 = dummy
    # pointer2 = head
        
    # for i in range(n):
    #     pointer2 = pointer2.next
            
    # while pointer2:
    #     pointer1 = pointer1.next
    #     pointer2 = pointer2.next
            
    # pointer1.next = pointer1.next.next
                
    # return dummy.next

    # Solution 1

    # length = 0
    # current = head

    # while current:
    #     current = current.next
    #     length += 1

    # if n > length:
    #     return None
        
    # current = head
        
    # if n == length:
    #     current = current.next
    #     return current
        
    # findIndex = length - n
    # index = 0

    # while current.next:
    #     if index == findIndex-1:
    #         current.next = current.next.next
    #         return head
    #     else:
    #         index += 1
            
    #     current = current.next