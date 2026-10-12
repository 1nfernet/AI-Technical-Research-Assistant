# AI Technical Research Assistant

An AI Engineering project designed to process technical documents and build the foundation for a Retrieval-Augmented Generation (RAG) system.

## Current Features

* Validate and load `.txt` documents.
* Reject missing, unsupported, or empty documents.
* Split text into overlapping chunks.
* Prefer paragraph boundaries when possible.
* Test document processing with `pytest`.

## Project Structure

```text
AI-Technical-Research-Assistant/
├── data/
│   └── raw/
│       └── materials_science.txt
├── src/
│   ├── ingestion.py
│   ├── chunking.py
│   └── main.py
├── tests/
│   ├── test_ingestion.py
│   ├── test_chunking.py
│   └── test_document_pipeline.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run the tests

```powershell
pytest -v
```

## Current Development Status

The current implementation covers document ingestion, text chunking, and integration testing.

The next development stages will introduce embeddings, vector storage, semantic retrieval, and LLM-based question answering.

## Disclaimer

This project is under active development. Features described as future stages are not yet implemented.
