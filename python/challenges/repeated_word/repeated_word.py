from data_structures.hashtable.hashtable import Hashtable


def repeated_word(string):
    ht = Hashtable()
    valid = "abcdefghijklmnopqrstuvwxyz "
    words = "".join(ch for ch in string.lower() if ch in valid).split()

    for word in words:
        if ht.contains(word):
            return word
        ht.add(word, word)

    return ""