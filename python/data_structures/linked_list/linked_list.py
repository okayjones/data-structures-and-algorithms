class Node:
    def __init__(self, value, next:Node=None):
        """Constructor for Node class

        Args:
            value (any): Value the Node represents
            next (Node, optional): Next Node in the list. Defaults to None.
        """
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head:Node=None):
        """Constructor for LinkedList

        Args:
            head ([Node, optional): Head Node in the list Defaults to None.
        """
        self.head = head

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

    def __str__(self) -> str:
        """String representation of the list

        Returns:
            str: description
        """
        current = self.head
        string = ''

        while current is not None:
            string += f"{{ {current.value} }} -> "

            current = current.next

        string += 'NULL'
        return string
