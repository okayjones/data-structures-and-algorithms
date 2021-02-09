# Challenge Summary
<!-- Short summary or background information -->
Fizz Buzz Tree

## Challenge Description

Given a binary tree, create a new tree where each node value is "fizz buzzed".

## Approach & Efficiency

Pre-order traversal was used to traverse through the existing tree, while building the new tree.

## Solution & Whiteboard

### Problem Domain

Given a binary tree, create a new tree where each node value is "fizz buzzed".

- input: binary tree
- output: binary tree

#### Visual

Preorder tree: [30, 10, 3, 11, 7, 21]
After fizzbuzz: ['FizzBuzz', 'Buzz', 'Fizz', '11', '7', 'Fizz']

### Algorithm // Pseudocode

```java
ALGO fizz_buzz_tree(tree)

    ALGO traverse(node)
        new_node <-- Node(fizz_buzz(node.value))
        if node.left
            node.left <-- traverse(node.left)
        if node.right
            node.right <-- traverse(node.right)
        OUTPUT < -- new_node
    
    new_tree <-- new BinaryTree
    new_tree.root <-- traverse(tree.root)

    OUTPUT <-- tree
        
ALGO fizz_buzz(int)
    //  standard fizz buzz
    OUTPUT <-- str
```

#### Big O

- Space: O(n)
- Time: O(n)
