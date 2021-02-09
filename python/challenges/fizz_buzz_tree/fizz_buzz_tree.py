def fizz_buzz_tree(tree):
    def fizz_buzz(value):
        if value % 15 == 0:
            return 'FizzBuzz'
        elif value % 3 == 0:
            return 'Fizz'
        elif value % 5 == 0:
            return 'Buzz'
        else:
            return str(value)

    def traverse(root):
        root.value = fizz_buzz(root.value)
        if root.left:
            traverse(root.left)
        if root.right:
            traverse(root.right)
    
    if tree.root:
        traverse(tree.root)

    return tree

