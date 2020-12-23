# Singly Linked List

Linked List implementation with Node and LinkedList classes

## Challenge

Create a Node class and Linked List class. The Linked List class has a variety of helpful methods.

## Approach & Efficiency

The Node and Linked List are both classes. The Node class contains a 'next' value, and the linked list class contains a head value. Together, these allow traversal through the list. Insert is O(1), while includes is O(n). Other list operations are O(n) for time and O(1) for space. 

## API

LinkedList

- `Insert`: Inserts a new Node with specified value to the head of the list.
- `Includes`: Returns a boolean based on a specified value existing in the list.
- `Append`: Appends a new Node to the end of the list.
- `insertBefore`: Inserts a new Node before a specified value.
- `insertAfter`: Inserts a new Node after a specified value.

## Whiteboard

![Whiteboard Image](../../assets/linkedlist_06.jpg)

![Whiteboard Image](../../assets/linkedlist_07.jpg)
