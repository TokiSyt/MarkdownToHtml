from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
	HTML = "html"
	LEAF = "leaf"
	TEXT = "text"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	IMAGE = "image"
	LINK = "link"

class TextNode:

	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url


	def __eq__(self, otherinstance):
		if not isinstance(otherinstance, TextNode):
			return False
		return self.url == otherinstance.url and self.text == otherinstance.text and self.text_type == otherinstance.text_type


	def __repr__(self):
		return f'TextNode("{self.text}", "{self.text_type}", {self.url})'

def text_node_to_html_node(text_node):
	if text_node.text_type == TextType.TEXT:
		return LeafNode(None, text_node.text)
	if text_node.text_type == TextType.BOLD:
		return LeafNode("b", text_node.text)
	if text_node.text_type == TextType.ITALIC:
		return LeafNode("i", text_node.text)
	if text_node.text_type == TextType.CODE:
		return LeafNode("code", text_node.text)
	if text_node.text_type == TextType.LINK:
		return LeafNode("a", text_node.text, {"href": text_node.url})
	if text_node.text_type == TextType.IMAGE:
		return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
	raise ValueError(f"Invalid text type: {text_node.text_type}")
