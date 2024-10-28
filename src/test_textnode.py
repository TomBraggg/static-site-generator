import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_no_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "google.com")
        self.assertEqual(node1, node2)

    def test_repr_no_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node1_repr = f'TextNode(This is a text node, {TextType.BOLD})'
        self.assertEqual(str(node1), node1_repr)

    def test_repr_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "google.com")
        node1_repr = f'TextNode(This is a text node, {TextType.BOLD}, google.com)'
        self.assertEqual(str(node1), node1_repr)


if __name__ == "__main__":
    unittest.main()
