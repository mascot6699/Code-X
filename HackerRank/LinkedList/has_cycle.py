def has_cycle(head):
    if not head:
        return False
    ptr1 = head
    ptr2 = head
    while(ptr1 and ptr2 and ptr2.next):
        ptr2 = ptr2.next.next
        ptr1 = ptr1.next
        if ptr1 == ptr2:
            return True
    return False