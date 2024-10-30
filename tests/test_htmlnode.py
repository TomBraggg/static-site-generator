import unittest
import mdconvert.htmlnode as htmlnode


class TestTextNode(unittest.TestCase):

    def test_props_to_html(self):
        my_node = htmlnode.HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        prop_string = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(prop_string, my_node.props_to_html())

    def test_props_to_html_blank_props(self):
        my_node = htmlnode.HTMLNode()
        prop_string = ''
        self.assertRaises(Exception)

    def test_repr(self):
        child_node = htmlnode.HTMLNode(tag="p", value="This is my value text")
        my_node = htmlnode.HTMLNode(tag="p",
                           value="This is my value text",
                           children=[child_node],
                           props = {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        node_string = 'HTMLNode(p, This is my value text, [HTMLNode(p, This is my value text, None, None)], {\'href\': \'https://www.google.com\', \'target\': \'_blank\'})'
        self.assertEqual(node_string, str(my_node))


if __name__ == "__main__":
    unittest.main()
