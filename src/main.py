from source_to_dest import source_to_dest
from generate_pages_recursive import generate_pages_recursive

def main():
	source_to_dest("static", "public")
	generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
	main()
