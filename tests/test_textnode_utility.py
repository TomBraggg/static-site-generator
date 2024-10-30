import unittest
import mdconvert.textnode_utility as text_util
import mdconvert.textnode as textnode
import mdconvert.htmlnode as htmlnode


class TestTextNode(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        test_text = "Test text"
        test_text_node = textnode.TextNode(test_text, textnode.TextType.TEXT)
        test_output = text_util.text_node_to_html_node(test_text_node)
        expected_output = htmlnode.HTMLNode(value=test_text)
        self.assertEqual(test_output, expected_output)

    def test_text_node_to_html_node_bold(self):
        test_text = "Test text"
        test_text_node = textnode.TextNode(test_text, textnode.TextType.BOLD)
        test_output = text_util.text_node_to_html_node(test_text_node)
        expected_output = htmlnode.HTMLNode(value=test_text, tag="b")
        self.assertEqual(test_output, expected_output)

    def test_text_node_to_html_node_italic(self):
        test_text = "Test text"
        test_text_node = textnode.TextNode(test_text, textnode.TextType.ITALIC)
        test_output = text_util.text_node_to_html_node(test_text_node)
        expected_output = htmlnode.HTMLNode(value=test_text, tag= "i")
        self.assertEqual(test_output, expected_output)

    def test_text_node_to_html_node_code(self):
        test_text = "Test text"
        test_text_node = textnode.TextNode(test_text, textnode.TextType.CODE)
        test_output = text_util.text_node_to_html_node(test_text_node)
        expected_output = htmlnode.HTMLNode(value=test_text, tag="code")
        self.assertEqual(test_output, expected_output)

    def test_text_node_to_html_node_link(self):
        test_text = "Test text"
        test_url = "google.com"
        test_text_node = textnode.TextNode(test_text, textnode.TextType.LINK, url=test_url)
        test_output = text_util.text_node_to_html_node(test_text_node)
        expected_output = htmlnode.HTMLNode(value=test_text, tag="a", props={
            "href": test_url,
        })
        self.assertEqual(test_output, expected_output)

    def test_text_node_to_html_node_image(self):
        test_text = "Test text"
        test_url = "google.com"
        test_text_node = textnode.TextNode(test_text, textnode.TextType.IMAGE, url=test_url)
        test_output = text_util.text_node_to_html_node(test_text_node)
        expected_output = htmlnode.HTMLNode(value=test_text, tag="img", props={
            "src": test_url
        })
        self.assertEqual(test_output, expected_output)

    def test_split_nodes_delimeter_code(self):
        test_node = textnode.TextNode("This is text with a `code block` section", textnode.TextType.TEXT)
        new_nodes = text_util._split_nodes_delimeter([test_node], "`", textnode.TextType.CODE)
        expected_result = [
            textnode.TextNode("This is text with a ", textnode.TextType.TEXT),
            textnode.TextNode("code block", textnode.TextType.CODE),
            textnode.TextNode(" section", textnode.TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_split_multiple_nodes(self):
        test_node_1 = textnode.TextNode("This is text with a `code block` section", textnode.TextType.TEXT)
        test_node_2 = textnode.TextNode("This is text with a **bold** section", textnode.TextType.TEXT)
        test_node_3 = textnode.TextNode("This is text with another `code block` section", textnode.TextType.TEXT)
        test_nodes = [test_node_1, test_node_2, test_node_3]
        new_nodes = []
        new_nodes = text_util._split_nodes_delimeter(test_nodes, "`", textnode.TextType.CODE)
        expected_result = [
            textnode.TextNode("This is text with a ", textnode.TextType.TEXT),
            textnode.TextNode("code block", textnode.TextType.CODE),
            textnode.TextNode(" section", textnode.TextType.TEXT),
            textnode.TextNode("This is text with a **bold** section", textnode.TextType.TEXT),
            textnode.TextNode("This is text with another ", textnode.TextType.TEXT),
            textnode.TextNode("code block", textnode.TextType.CODE),
            textnode.TextNode(" section", textnode.TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = text_util._extract_markdown_images(text)
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extracted_images, expected_result)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = text_util._extract_markdown_links(text)
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extracted_links, expected_result)

    def test_split_node_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        test_node = textnode.TextNode(text, textnode.TextType.TEXT)
        new_nodes = text_util._split_nodes_image([test_node])
        expected_result = [
            textnode.TextNode("This is text with a ", textnode.TextType.TEXT),
            textnode.TextNode("rick roll", textnode.TextType.IMAGE, url = "https://i.imgur.com/aKaOqIh.gif"),
            textnode.TextNode(" and ", textnode.TextType.TEXT),
            textnode.TextNode("obi wan", textnode.TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_split_node_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        test_node = textnode.TextNode(text, textnode.TextType.TEXT)
        new_nodes = text_util._split_nodes_link([test_node])
        expected_result = [
            textnode.TextNode("This is text with a link ", textnode.TextType.TEXT),
            textnode.TextNode("to boot dev", textnode.TextType.LINK, url="https://www.boot.dev"),
            textnode.TextNode(" and ", textnode.TextType.TEXT),
            textnode.TextNode("to youtube", textnode.TextType.LINK, url="https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_result = [
            textnode.TextNode("This is ", textnode.TextType.TEXT),
            textnode.TextNode("text", textnode.TextType.BOLD),
            textnode.TextNode(" with an ", textnode.TextType.TEXT),
            textnode.TextNode("italic", textnode.TextType.ITALIC),
            textnode.TextNode(" word and a ", textnode.TextType.TEXT),
            textnode.TextNode("code block", textnode.TextType.CODE),
            textnode.TextNode(" and an ", textnode.TextType.TEXT),
            textnode.TextNode("obi wan image", textnode.TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            textnode.TextNode(" and a ", textnode.TextType.TEXT),
            textnode.TextNode("link", textnode.TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(text_util.text_to_textnodes(text), expected_result)


if __name__ == "__main__":
    unittest.main()
