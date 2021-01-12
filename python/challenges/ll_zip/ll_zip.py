def zipLists(ll1, ll2):
    """Merge two linked lists by "zipping" them and alternating values.

    Args:
        ll1 (LinkedList)
        ll2 (LinkedList)

    Returns:
        LinkedList: The zipped linked list.
    """
    current1 = ll1.head
    current2 = ll2.head
    
    while current1 and current2:
        # save next pointers
        current1_next = current1.next
        current2_next = current2.next

        # swap next pointers
        current1.next = current2
        current2.next = current1_next

        #if list1 ends, connect rest of list2 
        if not current1_next:
            current1.next.next = current2_next
        
        # move current
        current1 = current1_next
        current2 = current2_next
    
    return ll1
