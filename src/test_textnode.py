import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text_node_to_html_node_text(self):
        test_text = "Test text"
        test_text_node = TextNode(test_text, TextType.TEXT)
        test_output = text_node_to_html_node(test_text_node)
        expected_output = HTMLNode(value=test_text)
        self.assertEqual(test_output, expected_output)

    def test_text_node_to_html_node_bold(self):
        test_text = "Test text"
        test_text_node = TextNode(test_text, TextType.BOLD)
        test_output = text_node_to_html_node(test_text_node)
        expected_output = HTMLNode(value=test_text, tag="b")
        self.assertEqual(test_output, expected_output)

    def test_text_node_to_html_node_italic(self):
        test_text = "Test text"
        test_text_node = TextNode(test_text, TextType.ITALIC)
        test_output = text_node_to_html_node(test_text_node)
        expected_output = HTMLNode(value=test_text, tag= "i")
        self.assertEqual(test_output, expected_output)

    def test_text_node_to_html_node_code(self):
        test_text = "Test text"
        test_text_node = TextNode(test_text, TextType.CODE)
        test_output = text_node_to_html_node(test_text_node)
        expected_output = HTMLNode(value=test_text, tag="code")
        self.assertEqual(test_output, expected_output)

    def test_text_node_to_html_node_link(self):
        test_text = "Test text"
        test_url = "google.com"
        test_text_node = TextNode(test_text, TextType.LINK, url=test_url)
        test_output = text_node_to_html_node(test_text_node)
        expected_output = HTMLNode(value=test_text, tag="a", props={
            "href": test_url,
        })
        self.assertEqual(test_output, expected_output)

    def test_text_node_to_html_node_image(self):
        test_text = "Test text"
        test_url = "google.com"
        test_text_node = TextNode(test_text, TextType.IMAGE, url=test_url)
        test_output = text_node_to_html_node(test_text_node)
        expected_output = HTMLNode(value="", tag="img", props={
            "src": test_url,
            "alt": test_text,
        })
        self.assertEqual(test_output, expected_output)


if __name__ == "__main__":
    unittest.main()
