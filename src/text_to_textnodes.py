from extract_markdown import *
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	if not old_nodes:
		return new_nodes

	for node in old_nodes:
		current_text = node.text
		while delimiter in current_text:
			delimiter_index_first = current_text.find(delimiter)
			delimiter_index_last = current_text.find(delimiter, delimiter_index_first + 1)

			if delimiter_index_first == -1 or delimiter_index_last == -1:
				new_nodes.append(node)
				break

			if delimiter_index_first > 0:
				new_nodes.append(TextNode(current_text[:delimiter_index_first], TextType.TEXT))

			content = current_text[delimiter_index_first + len(delimiter):delimiter_index_last]
			if content:
				new_nodes.append(TextNode(content, text_type))

			current_text = current_text[delimiter_index_last + len(delimiter):]

		if delimiter not in node.text:
			new_nodes.append(node)
		elif current_text:
			new_nodes.append(TextNode(current_text, TextType.TEXT))


	return new_nodes


def split_nodes_image(old_nodes):

	new_nodes = []
	for node in old_nodes:
		images = extract_markdown_images(node.text)
		if not images:
			new_nodes.append(node)
		else:
			current_text = node.text
			for image_alt, image_url in images:
				split_position = current_text.find(f"![{image_alt}]({image_url})")
				if split_position == -1:
					continue

				if split_position > 0:
					new_nodes.append(TextNode(current_text[:split_position], TextType.TEXT))

				new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

				current_text = current_text[split_position + len(f"![{image_alt}]({image_url})"):]
			if current_text:
				new_nodes.append(TextNode(current_text, TextType.TEXT))
	return new_nodes



def split_nodes_link(old_nodes):
	new_nodes = []
	for node in old_nodes:
		links = extract_markdown_links(node.text)

		if not links:
			new_nodes.append(node)
		else:
			current_text = node.text
			for link_text, link_url in links:
				split_position = current_text.find(f"[{link_text}]({link_url})")
				if split_position == -1:
					continue

				if split_position > 0:
					new_nodes.append(TextNode(current_text[:split_position], TextType.TEXT))

				new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

				current_text = current_text[split_position + len(f"[{link_text}]({link_url})"):]

			if current_text or len(new_nodes) == 2:
				new_nodes.append(TextNode(current_text, TextType.TEXT))

			if not current_text and len(new_nodes) == 2:
				new_nodes.append(TextNode("", TextType.TEXT))

	return new_nodes

def text_to_textnodes(text):

	nodes = [TextNode(text, TextType.TEXT)]
	nodes = split_nodes_image(nodes)
	nodes = split_nodes_link(nodes)
	nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
	nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
	nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
	nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
	return nodes
