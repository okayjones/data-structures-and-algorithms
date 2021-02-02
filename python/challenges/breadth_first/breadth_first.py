def breadth(tree) -> list:
    """Returns a breadth ordered list of binary tree values

    Args:
        tree (BinaryTree): Instance of BinaryTree

    Returns:
        list: list of values
    """
    queue = []
    result = []
    if tree.root:
        queue.append(tree.root)
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result
