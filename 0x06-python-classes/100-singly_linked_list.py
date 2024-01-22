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

    def __str__(self):
        """ to str an entire singlylinkedlist """
        prt = ""
        actual = self.__head
        while actual is not None:
            prt += str(actual.data)
            actual = actual.next_node
            if actual is not None:
                prt += '\n'
        return prt

    def sorted_insert(self, value):
        """ insert a value in the right place """
        if self.__head is None:
            self.__head = Node(value)
            return None
        head = self.__head
        if value <= self.__head.data:
            self.__head = Node(value, head)
            return None
        # if you use nude = head when you modify nude's attributes,
        # you modify head's also. but nude = another_node
        # do not affect head. think of it as pointer in C.
        # Maybe it's a ponter after all who knows xD
        # After quick search it is a pointer leeel
        # print("data:{} next:{}".format(head.data, head.next_node))
        nude = head
        while nude.next_node is not None:
            if nude.data <= value and nude.next_node.data >= value:
                nude.next_node = Node(value, nude.next_node)
                return None
            nude = nude.next_node
        nude.next_node = Node(value, None)
