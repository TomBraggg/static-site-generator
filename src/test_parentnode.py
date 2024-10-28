import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_to_html_single_child(self):
        test_leafnode_1 = LeafNode("Leafnode Value")
        children = [test_leafnode_1]
        test_parentnode = ParentNode(children, tag="p", props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        expected_result = '<p href="https://www.google.com" target="_blank">Leafnode Value</p>'
        self.assertEqual(expected_result, test_parentnode.to_html())

    def test_to_html_multi_child(self):
        test_leafnode_1 = LeafNode("Leafnode Value")
        test_leafnode_2 = LeafNode("Leafnode Value", tag="p1")
        test_leafnode_3 = LeafNode("Leafnode Value", tag="p1", props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        children = [test_leafnode_1, test_leafnode_2, test_leafnode_3]
        test_parentnode = ParentNode(children, tag="p", props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        expected_result = '<p href="https://www.google.com" target="_blank">Leafnode Value<p1>Leafnode Value</p1><p1 href="https://www.google.com" target="_blank">Leafnode Value</p1></p>'
        self.assertEqual(expected_result, test_parentnode.to_html())
        
    def test_to_html_parent_child(self):
        test_leafnode_1 = LeafNode("Leafnode Value")
        children_1 = [test_leafnode_1]
        test_parentnode_1 = ParentNode(children_1, tag="p", props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        children_2 = [test_parentnode_1]
        test_parentnode_2 = ParentNode(children_2, tag="div", props={
            "href": "bing.com",
            "target": "_blank",
        })
        expected_result = '<div href="bing.com" target="_blank"><p href="https://www.google.com" target="_blank">Leafnode Value</p></div>'
        self.assertEqual(expected_result, test_parentnode_2.to_html())

    def test_to_html_parent_child_with_leaves(self):
        test_leafnode_1 = LeafNode("Leafnode Value")
        test_leafnode_2 = LeafNode("Leafnode Value", tag="p1")
        test_leafnode_3 = LeafNode("Leafnode Value", tag="p1", props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        children_1 = [test_leafnode_1, test_leafnode_2, test_leafnode_3]
        test_parentnode_1 = ParentNode(children_1, tag="p", props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        children_2 = [test_parentnode_1]
        test_parentnode_2 = ParentNode(children_2, tag="div", props={
            "href": "bing.com",
            "target": "_blank",
        })
        expected_result = '<div href="bing.com" target="_blank"><p href="https://www.google.com" target="_blank">Leafnode Value<p1>Leafnode Value</p1><p1 href="https://www.google.com" target="_blank">Leafnode Value</p1></p></div>'
        self.assertEqual(expected_result, test_parentnode_2.to_html())
        

if __name__ == "__main__":
    unittest.main()
