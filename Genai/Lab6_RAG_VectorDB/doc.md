# Lab 6: Retrieval-Augmented Generation (RAG) System

## Objective
To build a RAG pipeline that retrieves relevant documents from a vector database and augments the prompt for generation.

## Theory
RAG combines **information retrieval** with **text generation**:
1. Documents are converted to embeddings (dense vectors)
2. Stored in a vector database (FAISS) for fast similarity search
3. At query time, the most relevant documents are retrieved
4. Retrieved context is injected into the prompt for the LLM to generate an informed answer

### Components
- **SentenceTransformer** — Embeds text into dense vectors
- **FAISS** — Facebook's library for efficient similarity search
- **Flan-T5** — Instruction-tuned text-to-text model for answer generation

## Code Explanation
1. Defines a 4-document knowledge base
2. Embeds documents using `all-MiniLM-L6-v2`
3. Builds a FAISS index with L2 distance
4. Encodes the query and retrieves top-2 matching documents
5. Constructs an augmented prompt with retrieved context
6. Generates answer using `google/flan-t5-base`

## Dependencies
```
sentence-transformers
faiss-cpu
numpy
transformers
```

## Expected Output
```
Retrieved Context: ['Retrieval-Augmented Generation combines...', ...]
Answer: Retrieval-Augmented Generation combines document retrieval with text generation
```

## References
- [Facebook FAISS](https://github.com/facebookresearch/faiss)
- [RAG Paper](https://arxiv.org/abs/2005.11401)
- [Sentence Transformers](https://www.sbert.net/)
