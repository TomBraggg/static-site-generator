import unittest
import mdconvert.htmlnode_utility as html_util


class TestHTMLNodeUtility(unittest.TestCase):
    def test_markdown_to_html_node_simple(self):
        md = """
# Header 1

This is bland inline text
"""
        html_result = html_util.markdown_to_html_str(md)
        expected_result = "<h1>Header 1</h1><p>This is bland inline text</p>"
        return self.assertEqual(html_result, expected_result)
    

    def test_markdown_to_html_node(self):
        md = """
# Header 1

This is my inline text, it has everything
Text which is **bold**
Text which is *italic*
Text which is `code`
Text containing links [google](https://www.google.com)
Text containing images ![richard](https://i.imgur.com/aKaOqIh.gif)

## Header 2

```
A block of code
Still a block of code
```

### Header 3

- Bread
- Eggs
- Milk

#### Header 4

1. I
2. **WILL**
3. Have
4. *Order*
"""
        html_result = html_util.markdown_to_html_str(md)
        expected_result = "<h1>Header 1</h1><p>This is my inline text, it has everything\nText which is <b>bold</b>\nText which is <i>italic</i>\nText which is <code>code</code>\nText containing links <a href=\"https://www.google.com\">google</a>\nText containing images <img src=\"https://i.imgur.com/aKaOqIh.gif\">richard</img></p><h2>Header 2</h2><code>A block of code\nStill a block of code\n</code><h3>Header 3</h3><ul><li>Bread</li><li>Eggs</li><li>Milk</li></ul><h4>Header 4</h4><ol><li>I</li><li><b>WILL</b></li><li>Have</li><li><i>Order</i></li></ol>"
        return self.assertEqual(html_result, expected_result)

    def test_extract_title(self):
        md = """
# Header 1

This is bland inline text
"""
        title = html_util.extract_title(md)
        expected_result = "Header 1"
        self.assertEqual(title, expected_result)


if __name__ == "__main__":
    unittest.main()
