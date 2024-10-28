import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from textnode_utility import text_node_to_html_node, split_nodes_delimeter


class TestTextNode(unittest.TestCase):
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

    def test_split_nodes_delimeter_code(self):
        test_node = TextNode("This is text with a `code block` section", TextType.TEXT)
        new_nodes = split_nodes_delimeter([test_node], "`", TextType.CODE)
        expected_result = [[
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" section", TextType.TEXT)
        ]]
        self.assertEqual(new_nodes, expected_result)

    def test_split_multiple_nodes(self):
        test_node_1 = TextNode("This is text with a `code block` section", TextType.TEXT)
        test_node_2 = TextNode("This is text with a **bold** section", TextType.TEXT)
        test_node_3 = TextNode("This is text with another `code block` section", TextType.TEXT)
        test_nodes = [test_node_1, test_node_2, test_node_3]
        new_nodes = []
        new_nodes = split_nodes_delimeter(test_nodes, "`", TextType.CODE)
        expected_result = [[
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" section", TextType.TEXT)
        ],
        [
            TextNode("This is text with a **bold** section", TextType.TEXT)
        ],
        [
            TextNode("This is text with another ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" section", TextType.TEXT)
        ]]
        print(f"new nodes: {new_nodes}")
        print(f"expected result : {expected_result}")
        self.assertEqual(new_nodes, expected_result)

if __name__ == "__main__":
    unittest.main()
