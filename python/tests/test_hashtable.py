from data_structures.hashtable.hashtable import Hashtable


def test_hashtable_create():
    hashtable = Hashtable()
    assert hashtable


def test_hashtable_predictable_hash():
    hashtable = Hashtable()
    initial = hashtable._hash("spam")
    secondary = hashtable._hash("spam")
    assert initial == secondary


def test_hashtable_in_range_hash():
    hashtable = Hashtable()
    actual = hashtable._hash("spam")
    assert 0 <= actual < hashtable.size


def test_hashtable_same_hash():
    hashtable = Hashtable()
    initial = hashtable._hash("listen")
    secondary = hashtable._hash("silent")
    assert initial == secondary


def test_hashtable_different_hash():
    hashtable = Hashtable()
    initial = hashtable._hash("glisten")
    secondary = hashtable._hash("silent")
    assert initial != secondary


def test_hashtable_get_none_key():
    hashtable = Hashtable()
    assert hashtable.get("key") == None


def test_hashtable_add_and_get():
    hashtable = Hashtable()
    hashtable.add("key", "value")
    assert hashtable.get("key") == "value"


def test_hashtable_collision():
    hashtable = Hashtable()
    hashtable.add("key", "value1")
    hashtable.add("yek", "value2")
    assert hashtable._hash("key") == hashtable._hash("yek")
    assert hashtable.get("key") == "value1"
    assert hashtable.get("yek") == "value2"


def test_hashtable_contains():
    hashtable = Hashtable()
    hashtable.add("key", "value")
    assert hashtable.contains("key") == True  