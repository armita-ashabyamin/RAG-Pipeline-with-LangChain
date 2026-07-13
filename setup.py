from setuptools import setup, find_packages

setup(
    name="rag-pipeline-langchain",
    version="0.1.0",
    description="A complete RAG pipeline using LangChain and Ollama for document Q&A",
    author="Armita Ashabyamin",
    author_email="armita.ay13792gmail.com",
    url="https://github.com/armita-ashabyamin/rag-pipeline-langchain",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.2.0",
        "langchain-community>=0.2.0",
        "langchain-core>=0.2.0",
        "langchain-huggingface>=0.0.3",
        "langchain-chroma>=0.1.0",
        "langchain-ollama>=0.1.0",
        "sentence-transformers>=2.2.0",
        "chromadb>=0.4.0",
        "pypdf>=3.17.0",
        "transformers>=4.30.0",
        "tiktoken>=0.4.0",
        "numpy>=1.24.0",
    ],
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="rag, langchain, ollama, embeddings, chroma, qa",
)
