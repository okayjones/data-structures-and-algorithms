from data_structures.hashtable.hashtable import Hashtable


def left_join(ht_left, ht_right):
    result = []
    for ll in ht_left._buckets:
        if ll.display():
            key, left_value = ll.display().pop()
            right_value = ht_right.get(key) if ht_right.contains(key) else None
            result.append([key, left_value, right_value])
    return result