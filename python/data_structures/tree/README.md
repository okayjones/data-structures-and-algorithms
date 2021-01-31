# Trees
<!-- Short summary or background information -->
Basic implementation of a Binary Search Tree

## Challenge
<!-- Description of the challenge -->
Create Node class, BinaryTree class, and BinarySearchTree classes. Implement pre_order, in_order, and post_order methods on the BinaryTree class. Implement add and contains on the BinarySearchTree class.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
BinaryTree methods were implemented using recursion. BinarySearchTree methods were implemented either recursively or iteratively.  
Adding a node to a BinarySearchTree is O(n).  
Searching for a node on a BinarySearchTree is O(h), where h=height.

## API
<!-- Description of each method publicly available in each of your trees -->
BinaryTree

- `pre_order()` - Returns an array of values, in root >> left >> right order
- `in_order()` - Returns an array of values, in left >> root >> right order
- `post_order()` - Returns an array of values, in left >> right >> root order

BinarySearchTree

- `add(value)` - Adds value to the tree
- `contains(value)` - Checks if value exists in the tree
