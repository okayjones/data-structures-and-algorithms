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

        # store last current in case shorter
        last_current1 = current1.next

        # move current
        current1 = current1_next
        current2 = current2_next
    
        # link rest of ll2 if ll1 was shorter
        if not current1:
            last_current1.next = current2
    
    return ll1
