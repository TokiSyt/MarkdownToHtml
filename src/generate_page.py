from markdown_blocks import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
	print(f"Genereating page from {from_path} to {dest_path} using {template_path}")

	with open(from_path) as rfp:
		fp = rfp.read()

	with open(template_path) as rtp:
		tp = rtp.read()

	html_node = markdown_to_html_node(fp)
	content = html_node.to_html()
	title = extract_title(fp)

	new_content = tp.replace("{{ Title }}", title).replace("{{ Content }}", content)

	os.makedirs(os.path.dirname(dest_path), exist_ok=True)

	with open(dest_path, 'w') as file:
		file.write(new_content)

	return None
