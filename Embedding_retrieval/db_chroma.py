import chromadb

client = chromadb.Client()
# client = chromadb.PersistentClient(
#     path="./chroma_db"
# )

collection = client.create_collection(
    name="insurance_docs"
)

collection.add(
    documents=[
        "Health insurance covers hospitalization.",
        "Motor insurance covers accidental damage.",
        "Travel insurance covers trip cancellation."
    ],

    ids=[
        "doc1",
        "doc2",
        "doc3"
    ]
)
'''
collection.add(
    documents=[
        "Health insurance covers hospitalization."
    ],
    ids=[
        "doc1"
    ],
    metadatas=[
        {
            "page":12,
            "source":"HealthPolicy.pdf",
            "product":"Health"
        }
    ]
)
'''

results = collection.query(
    query_texts=[
        "Hospital treatment claim"
    ],
    n_results=2
)
print(results)