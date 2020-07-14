#!/usr/bin/env python3

class AST(object):
    pass

class Operator(AST):

    def __init__(self, left, operator, right):
        self.left = left;
        self.token = operator;
        self.right = right;

class Num(AST):

    def __init__(self, token):
        self.token = token
        self.value = token.value