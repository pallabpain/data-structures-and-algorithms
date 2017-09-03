#!/usr/bin/env python

'''
Binary Tree implementation
'''

class BinaryTree(object):
    '''Represents a binary tree'''

    def __init__(self):
        self.root = None

    class Node(object):
        '''Represents a node in a binary tree'''
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return "[{0}<-{1}->{2}]".format(self.left, self.value, self.right)

    def insert(self, value):
        '''Inserts a node in a binary tree'''
        new_node = self.Node(value)
        if self.root is None:
            self.root = new_node
        else:
            node = self.root
            while True:
                if value < node.value:
                    if node.left is None:
                        node.left = new_node
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new_node
                        break
                    node = node.right

    def find(self, value):
        '''This method finds a node in the tree'''
        node, _ = self._find_with_parent(value)
        return node

    def _find_with_parent(self, value):
        '''This method finds and node and its parent'''
        node = self.root
        parent = None
        while node != None:
            if node.value == value:
                return node, parent
            parent = node
            node = node.left if value < node.value else node.right
        return None


    def __str__(self):
        return str(self.root)

    @property
    def height(self):
        '''Returns height of the binary tree'''
        def _height(root):
            if root is None:
                return 0
            return max(_height(root.left), _height(root.right)) + 1
        return _height(self.root)

    def remove(self, value):
        '''Removes a node from the tree'''
        node, parent = self._find_with_parent(value)
        if node is None:
            return None
        # If node has no right child, then
        # node's left replaces node
        if node.right is None:
            if parent is None:
                self.root = node.left
            else:
                if parent.value > node.value:
                    parent.left = node.left
                else:
                    parent.right = node.left
        # If node's right child has no left child
        # node's right child replaces node and
        # node's left becomes node's right's left
        elif node.right.left is None:
            node.right.left = node.left
            if parent is None:
                self.root = node.right
            if parent.value > node.value:
                parent.left = node.right
            else:
                parent.right = node.right
        # If node's right child has a left child
        # node's right child's left most child
        # replaces node
        else:
            leftmost = node.right.left
            leftmost_parent = node.right
            while leftmost.left is not None:
                leftmost_parent = leftmost
                leftmost = leftmost.left
            leftmost_parent.left = leftmost.right
            leftmost.left = node.left
            leftmost.right = node.right
            if parent is None:
                self.root = leftmost
            if parent.value > node.value:
                parent.left = leftmost
            else:
                parent.right = leftmost

    def level_order(self):
        '''Prints tree in level order'''
        queue = []
        node = self.root
        while node is not None:
            print node.value,
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            node = queue.pop(0) if queue else None


if __name__ == '__main__':
    tree = BinaryTree()
    nums = [5, 3, 4, 2, 7, 6, 8, 10, 9]
    for i in nums:
        tree.insert(i)
