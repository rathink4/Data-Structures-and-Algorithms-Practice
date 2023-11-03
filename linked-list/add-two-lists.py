def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    new = ListNode()
    start = new
    overflow = 0
    while(l1 and l2):
        value = l1.val + l2.val + overflow
        overflow = int(value/10)
        value = value % 10
        new.val = value
        if l1.next and l2.next:
            new.next = ListNode()
            new = new.next
        l1 = l1.next
        l2 = l2.next
    
    while(l1):
        new.next = ListNode()
        new = new.next
        value = l1.val + overflow
        overflow = int(value/10)
        value = value % 10
        new.val = value
        if not l1.next:
            new.next = None
        l1 = l1.next
    
    while(l2):
        new.next = ListNode()
        new = new.next
        value = l2.val + overflow
        overflow = int(value/10)
        value = value % 10
        new.val = value
        if not l2.next:
            new.next = None
        l2 = l2.next
    
    if overflow:
        new.next = ListNode()
        new = new.next
        new.val = overflow
        
    return start