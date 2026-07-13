
# RAG Pipeline with LangChain

A complete Retrieval-Augmented Generation (RAG) pipeline implementation using LangChain and Ollama.

## Overview

This project demonstrates how to build an intelligent question-answering system that reasons over your documents using:

- **Document Loading & Processing**: Ingest PDF documents and clean text
- **Chunking**: Split documents into manageable pieces with different strategies
- **Embeddings**: Convert text to vectors using `all-mpnet-base-v2`
- **Vector Storage**: Store embeddings in Chroma for similarity search
- **Retrieval**: Find relevant context with semantic search and MMR
- **LLM Integration**: Generate answers using Gemma 3 1B via Ollama
- **Re-ranking**: Improve retrieval quality with cross-encoder models

## Requirements

- Python 3.11.0+
- Ollama (for local LLM)

### Python Dependencies

```
langchain
langchain-community
langchain-core
langchain-huggingface
langchain-chroma
langchain-ollama
langchain-classic
pypdf
sentence-transformers
chromadb
transformers
tiktoken
numpy
```

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd rag-pipeline-langchain

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Ollama and pull the model
# Visit https://ollama.com to install Ollama
ollama pull gemma3:1b
```

## Project Structure

```
rag-pipeline-langchain/
├── data/                    # Place your PDF documents here
├── docs/
│   └── chroma/             # Vector database storage
├── notebooks/
│   └── rag_pipeline.ipynb  # Main Jupyter notebook
├── src/                     # Reusable Python modules
├── README.md
├── requirements.txt
└── .gitignore
```

## Usage

### 1. Prepare Your Documents

Place your PDF documents in the `data/` directory. The notebook expects:
- 2 PDF documents (15-25 pages each)
- Documents should contain specific/personal information not seen by the model

### 2. Run the Notebook

```bash
jupyter notebook notebooks/rag_pipeline.ipynb
```

### 3. Key Steps in the Pipeline

1. **Document Loading**: PDFs are loaded and text is cleaned
2. **Text Splitting**: Documents are chunked using recursive character splitting
3. **Embedding**: Text chunks are converted to vectors
4. **Vector Store**: Embeddings are stored in Chroma
5. **Retrieval**: Relevant chunks are retrieved based on queries
6. **Re-ranking**: Cross-encoder improves retrieval quality
7. **Generation**: LLM produces answers based on retrieved context

## Features

### Document Processing
- Automatic text cleaning
- Multiple splitting strategies (Character vs Recursive)
- Metadata preservation

### Retrieval Techniques
- **Similarity Search**: Basic semantic search
- **MMR (Maximum Marginal Relevance)**: Balanced relevance and diversity
- **Metadata Filtering**: Search within specific documents
- **Re-ranking**: Cross-encoder for improved accuracy

### Temperature Comparison
- **Low Temperature (0.01)**: More consistent, deterministic answers
- **High Temperature (0.7)**: More creative, varied responses

## Results

### Retrieval Comparison
| Method | Speed | Accuracy |
|--------|-------|----------|
| Basic Similarity Search | Fast | Good |
| MMR | Fast | Good with diversity |
| Re-ranking | Slower | Better |

### Temperature Trade-offs
| Temperature | Consistency | Creativity |
|-------------|-------------|------------|
| 0.01 | High | Low |
| 0.7 | Low | High |

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

---
