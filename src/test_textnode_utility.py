import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from textnode_utility import *


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
        expected_output = HTMLNode(value=test_text, tag="img", props={
            "src": test_url
        })
        self.assertEqual(test_output, expected_output)

    def test_split_nodes_delimeter_code(self):
        test_node = TextNode("This is text with a `code block` section", TextType.TEXT)
        new_nodes = split_nodes_delimeter([test_node], "`", TextType.CODE)
        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" section", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_split_multiple_nodes(self):
        test_node_1 = TextNode("This is text with a `code block` section", TextType.TEXT)
        test_node_2 = TextNode("This is text with a **bold** section", TextType.TEXT)
        test_node_3 = TextNode("This is text with another `code block` section", TextType.TEXT)
        test_nodes = [test_node_1, test_node_2, test_node_3]
        new_nodes = []
        new_nodes = split_nodes_delimeter(test_nodes, "`", TextType.CODE)
        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" section", TextType.TEXT),
            TextNode("This is text with a **bold** section", TextType.TEXT),
            TextNode("This is text with another ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" section", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = extract_markdown_images(text)
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extracted_images, expected_result)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = extract_markdown_links(text)
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extracted_links, expected_result)

    def test_split_node_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        test_node = TextNode(text, TextType.TEXT)
        new_nodes = split_nodes_image([test_node])
        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, url = "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_split_node_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        test_node = TextNode(text, TextType.TEXT)
        new_nodes = split_nodes_link([test_node])
        expected_result = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, url="https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, url="https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(text_to_textnodes(text), expected_result)


if __name__ == "__main__":
    unittest.main()
