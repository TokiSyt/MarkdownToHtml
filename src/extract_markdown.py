import re

def extract_markdown_images(text):

	image_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
	result = []

	for match_i in image_matches:
		result.append(tuple(match_i))

	return result

def extract_markdown_links(text):

	link_matches = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
	result = []
	for match_l in link_matches:
		result.append(tuple(match_l))

	return result

test1 = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")

print(test1)
