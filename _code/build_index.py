import os
import chromadb

#import tensorflow as tf
#import tensorflow_text as text
#import tensorflow_hub as hub


#embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3")


files = []

for root, dirs, filenames in os.walk("."):
    for file in filenames:
        files.append(os.path.join(root, file))

#filter out filew we dont want
files = [
    file for file in files
    if file.endswith(".md")
]

#filter out files from /.vscode and /chroma

files = [
    file for file in files
    if not file.startswith(".vscode") or file.startswith("chroma")
]


client = chromadb.PersistentClient("./chroma")

collection = client.get_or_create_collection("docs")

collection.add(
    documents = [files],
    ids = [str(i) for i in range(len(files))]
)