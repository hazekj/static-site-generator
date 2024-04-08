from textnode import TextNode

node = TextNode("This is a text node", "bold", "http://localhost")
node2 = node
print(node == node2)
print(node)
