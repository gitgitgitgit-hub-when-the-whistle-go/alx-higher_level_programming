#!/usr/bin/python3
""" Module docstring stop this docshi*t ffs """


class Node:
    """ class Node for a single linked list
    Args:
        data: data
        next_node: next_node
    Attributes:
        __data: the value of the linked list
        __next_node: the next node lmao
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError('data must be an interger')
        self.__data = data

    @next_node.setter
    def next_node(self, next_node):
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = next_node


class SinglyLinkedList:
    """ the actual list containing Nodes
    Args:
        head: the head of the list
    Attributes:
        __head: the head of the list
    """
    def __init__(self):
        self.__head = None

    def printsll(self):
        actual = self.__head
        i = 0
        while actual is not None:
            if i  > 12:
                exit
            print(actual.data)
            actual = actual.next_node
            i += 1

    @property
    def head(self):
        return self.__head


    def sorted_insert(self, value):
        if self.__head is None:
            print("empty")
            self.__head = Node(value)
            return
        head = Node(self.__head.data, self.__head.next_node)
        if value <= self.__head.data:
            self.__head = Node(value, head)
            return
        # if you use nude = head when you modify nude ,
        # you modify head also so create a diplicate.
        nude = Node(head.data, head.next_node)
        while nude.next_node is not None:
            if nude.data <= value and nude.next_node.data >= value:
                nude.next_node = Node(value, nude.next_node)
                return
            nude = Node(nude.next_node.data, nude.next_node.next_node)
        nude.next_node = Node(value, None)
        self.printsll()
