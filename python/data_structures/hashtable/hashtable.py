from linked_list import LinkedList


class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [LinkedList()] * size

    def _hash(self, key):
        total = sum([ord(ch) for ch in key])
        return (total * 7) % self.size

    def add(self, key, value):
        idx = self._hash(key)
        self._buckets[idx].add((key, value))

    def get(self, key):
        bucket = self._buckets[self._hash(key)]
        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            else:
                current = current.next

    def contains(self, key):
        bucket = self._buckets[self._hash(key)]
        current = bucket.head
        while current:
            if current.value[0] == key:
                return True
            else:
                current = current.next
        return False