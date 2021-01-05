def zipLists(ll1, ll2):
    current1 = ll1.head
    current2 = ll2.head
    
    while current1 and current2:
        current1_next = current1.next
        current2_next = current2.next

        current1.next = current2
        current2.next = current1_next

        current1 = current1_next
        current2 = current2_next
    
    return ll1
