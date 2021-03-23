from data_structures.hashtable.hashtable import Hashtable


def left_join(ht_left, ht_right):
    result = []

    for ll in ht_left._buckets:
        if ll.display():
            key, value = ll.display().pop()
            row = [key, value]

            if ht_right.contains(key):
                row.append(ht_right.get(key))
            else:
                row.append(None)
            result.append(row)

    return result