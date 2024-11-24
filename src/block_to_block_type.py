def block_to_block_type(markdown_block):

	if markdown_block:
		if markdown_block.startswith(("#", "##", "###", "####", "#####", "######")):
			return "heading"

		elif markdown_block.startswith("```") and markdown_block.endswith("```"):
			return "code"

		elif markdown_block.startswith(">"):
			return "quote"

		elif markdown_block.startswith("*") or markdown_block.startswith("-"):
			return "unordered_list"

		elif markdown_block[0].isdigit() and markdown_block[1] == "." and markdown_block[2] == " ":
			return "ordered_list"

		else:
			return "paragraph"
	else:
		return "paragraph"
