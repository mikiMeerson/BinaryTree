# מיקי מאירסון 207349010
# נעם תשובה 207576109

from __future__ import annotations
import random


class Point:
    def __init__(self, x=None, y=None):
        # TODO: if the x/y is zero then we will rand number
        # random.randint- Return a random integer N such that a <= N <= b.
        self.x = x if x is not None else random.randint(0, 100)
        self.y = y if y is not None else random.randint(0, 100)

    def __le__(self, other: int):
        """ This function overrides '<' operator for points
            Returns True if this point is to the right/same place in x aixs of the line, else False """
        return self.x <= other

    def __gt__(self, other: int):
        """ This function overrides '>' operator for points
            Returns True if this point is to the left  of the line, else False """
        return self.x > other

    def __lt__(self, other: Point):
        """ This function overrides '<' operator for points
            Returns True if this point is to the right of other point, else False """
        return self.x < other.x

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)


class Node:
    def __init__(self, key: Point):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None

    def __str__(self):
        return str(self.key)


class Tree:

    def __init__(self, root=None):
        self.root = root

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


def build_tree() -> Tree:
    """ Create 1000 random points and insert them into a binary search tree """
    t = Tree()
    for i in range(1000):
        new_node = Node(Point())
        t.insert(new_node)
    return t


def nearest_right_point(root, target):
    def _get_closest_node(node1, node2=None):
        """ Util func to get closest out of two nodes"""
        if node2 is None or node1.key < node2.key:
            return node1
        if node1.key < node2.key:
            return node1
        return node2

    # Eliminate side of tree that is to the left of the target
    while root.key <= target and root.right:
        root = root.right

    # If root is to the left of target and there is nothing to its right
    if root.key <= target:
        return None

    # Get nearest for left and right sub-trees
    right_closest = None
    left_closest = None

    if root.left:
        left_closest = nearest_right_point(root.left, target)
    left_closest = _get_closest_node(root, left_closest)

    if root.right:
        right_closest = nearest_right_point(root.right, target)
    right_closest = _get_closest_node(root, right_closest)

    return _get_closest_node(right_closest, left_closest)


def print_2d(root, space=0):
    """ This function prints the tree (left-most point is root) """
    if root is None:
        return

    # Increase distance between levels
    space += 10

    # Process right child
    print_2d(root.right, space)
    space_str = '\n'
    for i in range(10, space):
        space_str += ' '
    print(space_str + str(root.key))

    # Process left child
    print_2d(root.left, space)


if __name__ == '__main__':
    x0 = None
    while x0 is None:
        try:
            x0 = int(input("Type a number:"))
        except ValueError:
            print("This is not a whole number.")

    t = build_tree()

    print('Printing the tree - left-most node is the root:')
    print_2d(t.root)

    print(" Searching for {} nearest number to the right".format(x0))
    point = nearest_right_point(t.root, x0)
    print(point) if point else print(Point(0, 0))
