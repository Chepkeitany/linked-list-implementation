# -*- coding: utf-8 -*-
import unittest

from linked_list import Node


class NodeTestCase(unittest.TestCase):

    def test_node_str_representation_without_next(self):
        self.assertEqual(str(Node(9)), "Node(9) > /")

    def test_node_str_representation_with_next(self):
        n = Node(9)
        n.next = Node('X')
        self.assertEqual(str(n), "Node(9) > Node(X)")

    def test_node_equal_value(self):
        self.assertEqual(Node(1), Node(1))
        self.assertEqual(Node('hello'), Node('hello'))
        self.assertEqual(Node(True), Node(True))
        self.assertEqual(Node([1, 2, 3]), Node([1, 2, 3]))

    def test_node_not_equal_value(self):
        self.assertNotEqual(Node(1), Node(2))
        self.assertNotEqual(Node('hello'), Node('bye'))
        self.assertNotEqual(Node(True), Node(False))
        self.assertNotEqual(Node([1, 2, 3]), Node([3, 2, 1]))
