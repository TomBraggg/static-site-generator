import unittest
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_to_html_value_only(self):
        test_leafnode = LeafNode("Leafnode value")
        self.assertEqual("Leafnode value", test_leafnode.to_html())

    def test_to_html_value_tag(self):
        test_leafnode = LeafNode("Leafnode value", tag="p1")
        self.assertEqual('<p1>Leafnode value</p1>', test_leafnode.to_html())

    def test_to_html_full(self):
        test_leafnode = LeafNode("Leafnode value", tag="p1", props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual('<p1 href="https://www.google.com" target="_blank">Leafnode value</p1>', test_leafnode.to_html())


if __name__ == "__main__":
    unittest.main()
