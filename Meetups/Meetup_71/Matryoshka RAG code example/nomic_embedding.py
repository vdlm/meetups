## Using Nomic embedding model for query-document similarity
## https://huggingface.co/nomic-ai/nomic-embed-text-v1
from pathlib import Path

import numpy as np
from numpy.linalg import norm
from sentence_transformers import SentenceTransformer


def get_retrieval_results(matryoshka_dim = 1024):
    """Embed the documents with the chosen matryoshka dimension.

    Args:
        matryoshka_dim (int, optional): The embedding dimension size. Defaults to 1024.
    """
    model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", 
                                trust_remote_code=True,
                                truncate_dim=matryoshka_dim)


    sentences = Path("./docs.txt").read_text(encoding="utf-8").split("\n")
    sentences = ["search_document: " + s for s in sentences if s.strip() != ""]

    # sentences = ['search_document: TSNE is a dimensionality reduction algorithm created by Laurens van Der Maaten']
    doc_embeddings = model.encode(sentences, output_value='sentence_embedding')


    query = "What is a panda?"
    queries = [f'search_query: {query}']
    query_embeddings = model.encode(queries,  output_value='sentence_embedding')


    cosine_similarities = np.dot(query_embeddings, doc_embeddings.T) / (
        norm(query_embeddings, axis=1, keepdims=True)
        * norm(doc_embeddings, axis=1, keepdims=True).T
    )

    doc_ids = np.argsort(-cosine_similarities, axis=1)
    top_doc_ids = doc_ids[:, :10]

    for i, q in enumerate(queries):
        print(q)
        print("Top 5 most similar documents:")
        for doc_id in top_doc_ids[i]:
            print(f"{sentences[doc_id]} | Score: {cosine_similarities[i][doc_id]:.4f}")
        print()


if __name__ == "__main__":
    get_retrieval_results(matryoshka_dim=1024)
