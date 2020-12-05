#!/usr/bin/env python3

import sys
import bst
import logging

log = logging.getLogger(__name__)


class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def add(self, v):
        '''
        Example which shows how to override and call parent methods.  You
        may remove this function and overide something else if you'd like.
        '''
        super().add(v)
        return self.balance()

    def delete(self, v):
        super().delete(v)
        # return self.balance()
        return self

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''

        balanceValue = self.balanceCheck()

        if balanceValue == (-2):

            balanceValue = self.rc().balanceCheck()

            if balanceValue <= 0:
                return self.slr()
            else:
                return self.dlr()

        elif balanceValue == 2:

            balanceValue = self.lc().balanceCheck()

            if balanceValue >= 0:
                return self.srr()
            else:
                return self.drr()
        else:
            return self

    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        n1 = self.rc()
        self.set_rc(n1.lc())
        n1.set_lc(self)
        return n1

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        n1 = self.lc()
        self.set_lc(n1.rc())
        n1.set_rc(self)
        return n1

    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        self.set_rc(self.rc().srr())
        return self.slr()

    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        self.set_lc(self.lc().slr())
        return self.srr()

    def balanceCheck(self):
        leftRootLengh = self.lc().height() if not self.lc().is_empty() else 0
        rightRootLengh = self.rc().height() if not self.rc().is_empty() else 0
        # if it is a negativ number it is right heavy, is it positiv it is left heavy
        return leftRootLengh - rightRootLengh


if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
