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
        log.info("TODO@src/bst.py: implement postorder()")
        return []

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
        log.info("TODO@src/bst.py: implement bfs_order_star()")
        return []

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

    def privateFindNode(self, v):
        '''
        Expects that the value exist.
        Returns the node with that value.
        '''
        aLeftChild = True
        parentNode = None
        childNode = self
        while childNode.value() is not v:
            parentNode = childNode

            if childNode.value() > v:
                aLeftChild = True
                childNode = childNode.lc()
            else:
                aLeftChild = False
                childNode = childNode.rc()

        return parentNode, childNode, aLeftChild

    def delete(self, v):  # Lukas
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        if self.is_empty() or not self.is_member(v):
            return self
        else:
            # find the not to change
            parentNode, childNode, aLeftChild = self.privateFindNode(v)

            print(f"this is the node{childNode.value()}")

            # if it is a leaf
            if (childNode.lc().is_empty()) and (childNode.rc().is_empty()):

                # if it is the root then deleat it
                if childNode is self:
                    self is None

                if aLeftChild:
                    parentNode.set_lc() = None
                else:
                    parentNode.set_rc() = None
            # if it has no right child
            # elif childNode.rc() is None:
            #    pass

        return self


if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
