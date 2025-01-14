# Context Aware Conversational LLM

This repository contains a conversational retrieval system implemented using the LangChain framework. The system integrates a Language Model (LLM), a vector store, and a memory mechanism to provide contextual answers to user queries.

# Approach

- Language Model (LLM): The system uses GooglePalm as the language model, providing powerful language understanding capabilities.

- Vector Store: Qdrant is employed as the vector store for efficient storage and retrieval of document vectors.

- Memory Mechanism: The ConversationBufferMemory stores and retrieves conversation history, enabling the system to maintain context during interactions.

- Web API with Flask: The implementation includes a Flask web application that exposes an API endpoint (/ask) for users to submit queries and receive contextual responses.

  # Environment

- Python 3.6 or later
- Flask (> pip install Flask)
- LangChain (Install LangChain dependencies as needed)
