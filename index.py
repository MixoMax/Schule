import os
import time
import chromadb


client = chromadb.PersistentClient("./chroma")

collection = client.get_or_create_collection("schule")

#Folder Structure:
#/.vscode/ #ignore
#/.obxidian/ #ignore
#/S1/
#   /Bio/
#       -File_0.md
#       -File_1.md
#   /Boso/
#       -File_0.md
#       -File_1.md
#   /.../
#/S2/
#   /Bio/
#       -File_0.md
#       -File_1.md
#   /Boso/
#       -File_0.md
#       -File_1.md
#   /.../


#loop through all folders in the root folder
#if it is a folder, loop through all files in it

files = []

folders = [folder for folder in os.listdir(".") if os.path.isdir(folder)]

for folder in folders:
	#use os.walk to get all files in the folder
	for root, dirs, filenames in os.walk(folder):
		for filename in filenames:
			if filename.endswith(".md"):
				files.append(os.path.join(root, filename))

def filter_sentence(sentence:str) -> str or None:
	"""filter out markdown syntax to just the sentence

	return None if the sentence is empty after filtering
	"""

	remove_chars = ["#", "*", "_", "`", "[", "]", "(", ")", "!", "<", ">", "+", "-", "=", "~", "|", "  ", "\t", "\n"]

	for char in remove_chars:
		sentence = sentence.replace(char, "")

	if sentence == "" or sentence ==" ":
		return None
	else:
		return sentence

t1 = time.time()

counter = 0
for file in files:
	absolute_path = os.path.abspath(file)
	with open(file, "r", encoding="utf-8") as f:
		content = f.read()

	sentences = content.split("\n")
	senteces_new = []
	for sentence in sentences:
		senteces_new.extend(sentence.split("."))

	sentences = [filter_sentence(sentence) for sentence in senteces_new]

	senteces_new = [sentence for sentence in sentences if sentence is not None]
	metadatas = [{"path": absolute_path} for _ in senteces_new]
	ids = [str(idx) for idx in range(counter, counter + len(senteces_new))]


	if len(ids) == 0:
		continue

	collection.add(
		documents=senteces_new,
		ids=ids,
		metadatas=metadatas
	)
	print("Added file: " + file)
	counter += len(senteces_new)

print(f"build index in {(time.time() - t1):.2f} seconds (for {len(files)} files)")