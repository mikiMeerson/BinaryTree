from __future__ import annotations
import random


class Point:
    def __init__(self, x=None, y=None):
        # TODO: if the x/y is zero then we will rand number
        # random.randint- Return a random integer N such that a <= N <= b.
        self.x = x if x else random.randint(0, 100)
        self.y = y if y else random.randint(0, 100)

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


class Node:
    def __init__(self, key: Point):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None


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


def nearest_right_point(t: Tree, x0: int) -> Point:
    p = t.root
    while (p.key <= x0 and p.right):
        p = p.right

    if p.key > x0:
        return(p.key)
    else:  # not p.right:
        return Point(1, 1)


if __name__ == '__main__':
    x0 = random.randint(0, 100)
    point = nearest_right_point(build_tree(), x0)
    print("{0},{1}".format(point.x, point.y))
