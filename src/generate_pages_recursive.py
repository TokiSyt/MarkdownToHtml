import os
from markdown_blocks import markdown_to_html_node
from extract_title import extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

	for item in os.listdir(dir_path_content):

		item_path = os.path.join(dir_path_content, item)

		if os.path.isfile(item_path) and item_path.endswith(".md"):

			with open(item_path) as item_p:
				md_file = item_p.read()

			title = extract_title(md_file)
			html_n = markdown_to_html_node(md_file)
			content = html_n.to_html()

			with open(template_path) as item_t:
				t_path = item_t.read()

			rel_path = os.path.relpath(item_path, dir_path_content)
			dest_path = os.path.join(dest_dir_path, rel_path)
			dest_path = dest_path.replace('.md', '.html')
			new_html = t_path.replace("{{ Title }}", title).replace("{{ Content }}", content)

			os.makedirs(os.path.dirname(dest_path), exist_ok=True)

			with open(dest_path, 'w') as dest_file:
				dest_file.write(new_html)


		elif os.path.isdir(item_path):
			new_dest_dir = os.path.join(dest_dir_path, item)
			os.makedirs(new_dest_dir, exist_ok=True)
			generate_pages_recursive(item_path, template_path, new_dest_dir)

	return None
