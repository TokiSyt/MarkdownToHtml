import shutil
import os

def source_to_dest(source_path, dest_path):

	if os.path.exists(dest_path):
		shutil.rmtree(dest_path)
	os.mkdir(dest_path)

	for item in os.listdir(source_path):
		src = os.path.join(source_path, item)
		dest = os.path.join(dest_path, item)


		if os.path.isfile(src):
			shutil.copy(src, dest)
		else:
			os.mkdir(dest)
			source_to_dest(src, dest)
