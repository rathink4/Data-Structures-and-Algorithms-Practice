def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    curr = head
    count = 0

    while(curr):
        curr = curr.next
        count += 1

    remove = count - n - 1
    count = 0
    curr = head

    if remove == -1:
        return head.next

    while(curr):
        if count == remove:
            curr.next = curr.next.next
            break
        curr = curr.next
        count += 1
    
    return head