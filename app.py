import random


class Point:
    def __init__(self, x=None, y=None):
        self.x = x if x else random.randint(0, 101)
        self.y = y if y else random.randint(0, 101)

    def __ge__(self, other):
        """ This function overrides '<' operator for points
            Returns True if this point is to the left of other point, else False """
        return self.x > other.x

    def __le__(self, other):
        """ This function overrides '<' operator for points
            Returns True if this point is to the right of other point, else False """
        return self.x < other.x


class Node:
    def __init__(self, key: Point):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        """ Insert given node to appropriate place in the tree"""
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node


def build_tree(t: Tree):
    """ Create 100 random points and insert them into a binary search tree """
    for i in range(100):
        new_node = Node(Point())
        t.insert(new_node)