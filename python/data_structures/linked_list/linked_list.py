class Node:
    def __init__(self, value, next=None):
        """Constructor for Node class

        Args:
            value (any): Value the Node represents
            next (Node, optional): Next Node in the list. Defaults to None.
        """
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        """Constructor for LinkedList

        Args:
            head ([Node, optional): Head Node in the list Defaults to None.
        """
        self.head = head

    def __str__(self) -> str:
        """String representation of the list

        Returns:
            str: description
        """
        current = self.head
        string = ""

        while current is not None:
            string += f"{{ {current.value} }} -> "

            current = current.next

        string += "NULL"
        return string

    def insert(self, value):
        """Insert a value into the head of the list.

        Args:
            value (any): Value the new Node represents
        """
        node = Node(value)

        if self.head is not None:
            node.next = self.head

        self.head = node

    def includes(self, value) -> bool:
        """Searches the list for a value

        Args:
            value (any): Value to search in the list

        Returns:
            bool: Returns whether value exists
        """
        current = self.head

        while current is not None:
            if current.value == value:
                return True

            current = current.next

        return False

    def append(self, value):
        """appends a new node to the end of the list

        Args:
            value (any): value to append
        """
        node = Node(value)
        current = self.head

        if self.head is None:
            self.head = node
            return

        while current.next is not None:
            current = current.next

        current.next = node

    def insertBefore(self, value, newVal):
        """Inserts newVal into the list, before a specified value. 

        Args:
            value (any): value to insert before
            newVal (any): value to insert

        Raises:
            Exception: raised if value not present
        """
        current = self.head

        if current.value is value:
            self.insert(newVal)
            return
            
        while current is not None:
            if current.next.value is value:
                node = Node(newVal, current.next)
                current.next = node
                return
            current = current.next

        raise Exception(f"Value {{ {value} }} not present in list")

    def insertAfter(self, value, newVal):
        """Inserts newVal into the list, after a specified value. 

        Args:
            value (any): value to insert after
            newVal (any): value to insert

        Raises:
            Exception: raised if value not present
        """
        current = self.head

        while current is not None:
            if current.value is value:
                node = Node(newVal, current.next)
                current.next = node
                return
            current = current.next

        raise Exception(f"Value {{ {value} }} not present in list")

    def kthFromEnd(self, k:int):
        """Returns the kth number from end in the list.

        Args:
            k (int): number from end

        Raises:
            Exception: out of bounds

        Returns:
            (any): value
        """
        current = self.head

        list = []

        while current is not None:
            list.append(current) 
            current = current.next

        size = len(list)  
        if k < size:
            return list[size -k -1].value
        
        raise Exception()

