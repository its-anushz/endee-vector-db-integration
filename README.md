# Endee Vector Database Integration

A hands-on infrastructure-focused project exploring the setup, deployment, and API surface of the Endee open-source vector database, with designed ingestion and retrieval pipelines aligned to current OSS capabilities.

## Project Overview

This project focuses on integrating and evaluating the Endee open-source vector database from an infrastructure and system-design perspective.

The primary goal was to:
- Build and run Endee OSS locally from source using Docker
- Validate the exposed HTTP API surface
- Design clean vector ingestion and retrieval pipelines
- Adapt the system design based on real API constraints

Rather than assuming full CRUD-style APIs, this project emphasizes correct engineering practice: probing supported endpoints, validating HTTP methods, and designing extensible pipelines that align with the current capabilities of Endee OSS.
## Why Endee?

Endee is a high-performance vector database focused on efficient similarity search and scalable AI infrastructure.

This project uses Endee because:
- It represents a modern, systems-level approach to vector databases
- It exposes a C++-based core with Dockerized deployment
- It provides an opportunity to work close to infrastructure rather than abstracted SDKs

The intent was not to build a UI-heavy application, but to understand how a vector database behaves at the API and system boundary level.
## System Architecture

The system is structured into three conceptual layers:

1. **Vector Database Layer**
   - Endee OSS built and run from source using Docker
   - Provides internal vector indexing and a browser-accessible UI

2. **Embedding Layer**
   - Python-based embedding pipeline using SentenceTransformers
   - Designed to generate dense vector representations for documents and queries

3. **Integration Layer**
   - Python modules for ingestion and retrieval
   - Structured to interact with Endee via HTTP once write/query APIs are available

## What Works Today

The following components are fully functional and validated:

- Local build and deployment of Endee OSS using Docker
- Health check and service availability verification
- API surface discovery using HTTP OPTIONS and GET requests
- Embedding pipeline using pretrained transformer models
- Clean Python project structure for ingestion and retrieval logic

All infrastructure setup and API validation steps were performed against a running Endee instance.

## Endee OSS API Limitations

During development, the Endee OSS HTTP API was systematically validated using OPTIONS and GET requests.

Findings:
- Endee OSS currently exposes read-only HTTP endpoints
- Vector ingestion (write) APIs are not available over HTTP
- Programmatic semantic search APIs are not exposed via JSON-based endpoints
- Certain routes serve browser-based UI responses rather than machine-readable JSON

As a result, vector ingestion and semantic retrieval are not executed at runtime in this project. Instead, they are implemented as designed integration modules, ready to be activated once Endee exposes write/query APIs.

## Ingestion & Retrieval Design (Planned)

Although runtime ingestion and retrieval are not supported by the current Endee OSS API, this project includes fully designed pipelines:

### Ingestion Design
- Document loading from structured JSON sources
- Transformer-based embedding generation
- Index-based vector storage model aligned with Endee’s architecture

### Retrieval Design
- Query embedding generation
- Top-k similarity search against indexed vectors
- Metadata-based result interpretation

These components are implemented in code and documented to demonstrate intended integration behavior once supported by the underlying database.

## Setup & Execution

### Prerequisites
- Docker & Docker Compose
- Python 3.9+
- Git

### Steps
1. Clone the repository
2. Build and run Endee OSS using Docker
3. Verify service health via HTTP endpoints
4. Review embedding, ingestion, and retrieval modules

> Note: Ingestion and retrieval scripts are provided for design completeness and are not executed due to current API limitations.

## Learnings & Engineering Takeaways

This project reinforced several real-world engineering principles:

- Infrastructure tools must be validated, not assumed
- API surface discovery is critical before system integration
- Designing for extensibility is more important than forcing incomplete features
- Honest documentation is preferable to misleading demos

The project prioritizes correctness, clarity, and system-level understanding over superficial functionality.


The architecture intentionally separates concerns so that future API support can be integrated without restructuring the system.
