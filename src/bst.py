#!/usr/bin/env python3

import bt
import sys
import logging

log = logging.getLogger(__name__)


class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        '''
        Returns true if the value `v` is a member of the tree.
        '''
        if self.is_empty():
            return False
        else:
            if v < self.value():
                if self.lc() == None:
                    return False
                return self.lc().is_member(v)
            elif v > self.value():
                if self.rc() == None:
                    return False
                return self.rc().is_member(v)
            else:
                return True

    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''
        if self.is_empty():
            return 0
        else:
            return 1 + self.rc().size() + self.lc().size()

    def height(self):
        '''
        Returns the height of the tree.
        '''

        if self.is_empty():
            return 0
        else:
            return 1 + max(self.lc().height(), self.rc().height())

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.value()] + self.lc().preorder() + self.rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return []
        return self.lc().inorder() + [self.value()] + self.rc().inorder()

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.is_empty():
            return []
        return self.lc().inorder() + self.rc().inorder() + [self.value()]

    def noneroot(self, index, size):
        exlution = []

        left_child = right_child = index

        while left_child <= size:
            left_child = (2 * left_child) + 1
            exlution.append(left_child)

        while right_child <= size:
            right_child = (2 * right_child) + 1
            exlution.append(right_child)

        return exlution

    def bfs_list(self):

        bfsqueue = []
        treequeue = []

        treequeue.append(self)

        while(len(treequeue) > 0):

            bfsqueue.append(treequeue.pop(0))

            node = treequeue.pop(0)

            # Enqueue left child
            if node.lc() is not None:
                treequeue.append(node.lc())

                # Enqueue right child
            if node.rc() is not None:
                treequeue.append(node.rc())

        return bfsqueue

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).

        For example, consider the following tree `t`:
                    10
              5           15
           *     *     *     20

        The output of t.bfs_order_star() should be:
        [ 10, 5, 15, None, None, None, 20 ]
        '''
        if self.is_empty():
            return []
        else:

            totalsize = ((2**self.height()) - 1)
            # sätter alla index lika men None
            bfsqueue = [None] * totalsize
            treequeue = self.bfs_list()

            exlution = []

            for index in range(totalsize):

                if index not in exlution:

                    node = treequeue.pop(0)

                    bfsqueue[index] = node.value()

                    # checking if node has a left child
                    if node.lc().is_empty():
                        index_left = (2 * index) + 1
                        exlution += self.noneroot(index, totalsize)

                        # checking if node has a right child
                    elif node.rc().is_empty():
                        index_right = (2 * index) + 2
                        exlution += self.noneroot(index_right, totalsize)

            return bfsqueue

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.value():
            return self.cons(self.lc().add(v), self.rc())
        if v > self.value():
            return self.cons(self.lc(), self.rc().add(v))
        return self
    """
    need to find out why my recuriosn dont work
    def findTheMostSmallsest(self):
        if not self.lc().is_empty():
            print(self.value())
            return self.lc().findTheMostSmallsest()
    """

    def findTheSmallsestNodeOnTheRight(self):
        # node = self
        node = self.rc()
        while not node.lc().is_empty():
            node = node.lc()
        return node

    def removeNode(self):
        """
        4 casese to remove a node

        1 - it is a leaf

        2 - it has only left child

        3 - it has only right child

        4 - it has both childern
        """
        # is a leaf
        if self.lc().is_empty() and self.rc().is_empty():

            self.set_value(None)
            return self.cons(None, None)

        elif self.lc().is_empty() and not self.rc().is_empty():

            self.set_value(self.rc().value())
            return self.cons(self.rc().lc(), self.rc().rc())

        elif not self.lc().is_empty() and self.rc().is_empty():

            self.set_value(self.lc().value())
            return self.cons(self.lc().lc(), self.lc().rc())

        elif not self.lc().is_empty() and not self.rc().is_empty():

            # self.smalestNode = self.rc().findTheSmallsestNodeOnTheRight()
            self.smalestNode = self.findTheSmallsestNodeOnTheRight()
            self.set_value(self.smalestNode.value())
            self.smalestNode.removeNode()

            return self

    def delete(self, v):  # Lukas
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        if self.is_empty() or not self.is_member(v):
            return self
        elif v < self.value():
            return self.cons(self.lc().delete(v), self.rc())
        elif v > self.value():
            return self.cons(self.lc(), self.rc().delete(v))
        else:
            return self.removeNode()


if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
