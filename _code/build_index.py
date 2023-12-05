import os
import time
import chromadb

import tensorflow as tf
import tensorflow_text as text
import tensorflow_hub as hub

t_start = time.time()

files = []

for root, dirs, filenames in os.walk("."):
    for file in filenames:
        files.append(os.path.join(root, file))

#filter out files we dont want
files = [
    file for file in files
    if file.endswith(".md")
]

#filter out files from /.vscode and /chroma

files = [
    file for file in files
    if not file.startswith(".vscode") or file.startswith("chroma")
]



def filter_sentences(sentences:str) -> list[str]:
    """filter an array of sentences to remove unwanted characters and empty strings"""
    
    sentences = [
        sentence.strip() for sentence in sentences
    ]
    
    #remove chars from markdown syntax to only get the text
    remove_chars = ["#", "*", "`", "_", "[", "]", "(", ")", ">", "<", "-", "+", "=", "~", "|", "\\", "/", "!", "."]
    
    for char in remove_chars:
        sentences = [
            sentence.replace(char, "") for sentence in sentences
        ]
    
    sentences = [
        sentence for sentence in sentences
        if len(sentence) > 0
    ]
    
    return sentences

embed = hub.load("./_code/embed_model/")

class FileEntry():
    sentences: list[str]
    abs_path: str
    metadata: dict[str, str]
    
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.metadata = {
            "path": os.path.abspath(file_path)
        }
    
    def read_file_to_sentences(self):
        with open(self.file_path, "r") as f:
            sentences = f.readlines()
        
        #split by "."
        
        sentences = [
            sentence.split(".") for sentence in sentences
        ]
        
        #flatten
        sentences = [
            sentence for sublist in sentences for sentence in sublist
        ]
        
        sentences = filter_sentences(sentences)
        
        self.sentences = sentences
        

    def embed_sentences(self):
        embeddings = embed(self.sentences)
        self.embedded_sentences = embeddings.numpy().tolist()


client = chromadb.PersistentClient("./chroma")

collection: chromadb.Collection = client.get_or_create_collection("docs")


global_id_counter = 0
for idx, file in enumerate(files):
    file_entry = FileEntry(file)
    file_entry.read_file_to_sentences()
    #file_entry.embed_sentences()
    
    if len(file_entry.sentences) == 0:
        continue

    collection.add(
        documents = file_entry.sentences,
        #embeddings = file_entry.embedded_sentences,
        metadatas = [file_entry.metadata for _ in range(len(file_entry.sentences))],
        ids = [str(global_id_counter + i) for i in range(len(file_entry.sentences))]
    )
    
    print(f"Added {len(file_entry.sentences)} sentences from {file_entry.metadata['path']}")
    
    global_id_counter += len(file_entry.sentences)

print(f"built index in {time.time() - t_start:.2f} seconds")