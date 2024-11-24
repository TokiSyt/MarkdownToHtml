def extract_title(markdown):

	for line in markdown.splitlines():
		line = line.strip()
		if line.startswith("#") and len(line) > 1:
			return line.lstrip("#").strip()

	raise Exception("Title must have h1 tag")
