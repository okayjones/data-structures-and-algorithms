class Animal():
    def __init__(self, type:str, name:str):
        """Constructor for animal objects

        Args:
            type (str): cat or dog
            name (str): name of animal
        """
        self.type = type
        self.name = name

class AnimalShelter():
    def __init__(self):
        """constructor for Animal Shelter
        """
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal:Animal):
        """Add an animal to the animal shelter

        Args:
            animal (Animal): Animal to  add

        Raises:
            Exception: type not valid
        """
        if animal.type == "cat":
            self.cats.enqueue(animal)
        elif animal.type == "dog":
            self.dogs.enqueue(animal)
        else:
            raise Exception("Animal type not valid")

    def dequeue(self, pref:str) -> Animal:
        """Takes an animal from the shelter

        Args:
            pref (str): dog or cat

        Returns:
            [Animal]: dog or cat
        """
        try:
            if pref == "cat":
                return self.cats.dequeue()
            elif pref == "dog":
                return self.dogs.dequeue()
        except Exception:
            return None


#### FIGURE OUT HOW TO IMPORT THIS INSTEAD ####
class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue():
    def __init__(self, front=None):
        self.front = front
        self.rear = None

    def enqueue(self, value):
        node = Node(value)

        if self.isEmpty():
            self.front = node
            self.rear = node
        else:    
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            return self.front.value

    def isEmpty(self):
        return self.front == None