import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div", "Hello", None, {"id": "first", "href": "https://www.me.com"}
        )
        self.assertEqual(node.props_to_html(), ' id="first" href="https://www.me.com"')


if __name__ == "__main__":
    unittest.main()
