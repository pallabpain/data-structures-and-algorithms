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
        '''This function finds a node in the tree'''
        node = self.root
        while node != None:
            if node.value == value:
                return node, 'Found'
            node = node.left if value < node.value else node.right
        return node

    def __str__(self):
        return str(self.root)
















if __name__ == '__main__':
    tree = BinaryTree()
    nums = [5, 3, 4, 2, 7, 6, 8, 10, 9]
    for i in nums:
        tree.insert(i)
    print tree





