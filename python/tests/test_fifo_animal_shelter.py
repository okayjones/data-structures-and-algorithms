import pytest
from challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter, Animal
from challenges.fifo_animal_shelter import __version__

def test_version():
    assert __version__ == "0.1.0"

def test_animal_enqueue_one():
    animal_type = "cat"
    animal_name = "cat1"
    animal = Animal(animal_type, animal_name)
    shelter = AnimalShelter()
    shelter.enqueue(animal)
    actual = shelter.cats.peek()
    expected = animal
    assert actual == expected

def test_animal_enqueue_many():
    animal_type1 = "dog"
    animal_name1 = "dog1"
    animal_type2 = "cat"
    animal_name2 = "cat2"
    animal1 = Animal(animal_type1, animal_name1)
    animal2 = Animal(animal_type2, animal_name2)
    shelter = AnimalShelter()
    shelter.enqueue(animal1)
    shelter.enqueue(animal2)
    actual = shelter.cats.peek()
    expected = animal2
    assert actual == expected

def test_animal_enqueue_bad_type():
    animal_type = "frog"
    animal_name = "frog"
    animal = Animal(animal_type, animal_name)
    shelter = AnimalShelter()
    with pytest.raises(Exception):
        shelter.enqueue(animal)

def test_animal_dequeue_one():
    animal_type = "cat"
    animal_name = "cat1"
    animal = Animal(animal_type, animal_name)
    shelter = AnimalShelter()
    shelter.enqueue(animal)
    actual = shelter.dequeue("cat")
    expected = animal
    assert actual == expected

def test_animal_dequeue_many():
    animal_type1 = "dog"
    animal_name1 = "dog1"
    animal_type2 = "dog"
    animal_name2 = "dog2"
    animal1 = Animal(animal_type1, animal_name1)
    animal2 = Animal(animal_type2, animal_name2)
    shelter = AnimalShelter()
    shelter.enqueue(animal1)
    shelter.enqueue(animal2)
    shelter.dequeue("dog")
    actual = shelter.dequeue("dog")
    expected = animal2
    assert actual == expected

def test_animal_dequeue_many_mixed():
    animal_type1 = "dog"
    animal_name1 = "dog1"
    animal_type2 = "cat"
    animal_name2 = "cat2"
    animal1 = Animal(animal_type1, animal_name1)
    animal2 = Animal(animal_type2, animal_name2)
    shelter = AnimalShelter()
    shelter.enqueue(animal1)
    shelter.enqueue(animal2)
    shelter.dequeue("cat")
    actual = shelter.dequeue("dog")
    expected = animal1
    assert actual == expected

def test_animal_dequeue_many_empty():
    animal_type1 = "dog"
    animal_name1 = "dog1"
    animal_type2 = "dog"
    animal_name2 = "dog2"
    animal1 = Animal(animal_type1, animal_name1)
    animal2 = Animal(animal_type2, animal_name2)
    shelter = AnimalShelter()
    shelter.enqueue(animal1)
    shelter.enqueue(animal2)
    shelter.dequeue("dog")
    shelter.dequeue("dog")
    actual = shelter.dequeue("dog")
    expected = None
    assert actual == expected