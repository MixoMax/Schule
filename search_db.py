import chromadb


client = chromadb.PersistentClient("./chroma")

collection = client.get_or_create_collection("schule")

q = str(input("Query: "))

results = collection.query(
    query_texts=[q],
    n_results=10,
)

# results = {"ids": [["1", "2",  "3"]],
#               "distances": [[int]]
#               "metadatas": [[{"path": "path/to/file"}]]}
#               "documents": [["sentence 1", "sentence 2", "sentence 3"]]}

#we are interested in the metadata
metadatas = results["metadatas"][0]

paths = [metadata["path"] for metadata in metadatas]

distances = results["distances"][0]

sentences = [document for document in results["documents"][0]]

    
max_len_path = max([len(path) for path in paths])
max_total_width = 130
max_len_sentence = max_total_width - max_len_path - 4

print("Sentence".ljust(max_len_sentence+3), "Path".ljust(max_len_path+1), "Distance", sep=" | ")
print("-" * max_total_width)

for i in range(len(sentences)):
    sentence = sentences[i][:max_len_sentence]
    if len(sentences[i]) > max_len_sentence:
        sentence += "..."
    print(sentence.ljust(max_len_sentence+3), paths[i].ljust(max_len_path+1), f"{distances[i]:.3f}", sep=" | ")