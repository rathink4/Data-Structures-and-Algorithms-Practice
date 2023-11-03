def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    rev = None
    while(curr):
        temp = curr.next
        curr.next = rev
        rev = curr
        curr = temp
    
    return rev