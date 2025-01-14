# Import necessary modules and classes
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from flask import Flask, request, jsonify
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Qdrant
from langchain.llms import GooglePalm
from langchain.llms import CTransformers

# Define the path to the Faiss database for vector storage
DB_FAISS_PATH = 'vectorstore/db_faiss'

# Initialize a Flask web application
app = Flask(__name__)

# Function to load the language model (LLM)
def load_llm():
    # Instantiate GooglePalm LLM with the provided API key
    llm = GooglePalm(google_api_key="AIzaSyD6Vlv1bz3QokAbLQTIswbz_afVvEQwxUo")
    return llm

# Instantiate a CSVLoader to load data from a CSV file
loader = CSVLoader(file_path=r"E:\chabhi\chatwithcsv\chatwithcsv\bigBasketProducts.csv", encoding="utf-8", csv_args={'delimiter': ','})
data = loader.load()

# Create embeddings using the HuggingFaceEmbeddings class
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})

# Create a Qdrant vector store from the loaded data and embeddings
qdrant = Qdrant.from_documents(data, embeddings, location=":memory:", collection_name="my_documents")

# Instantiate the language model (LLM)
llm = load_llm()

# Create a ConversationBufferMemory for storing and retrieving conversation history
memory = ConversationBufferMemory(memory_key="chat_history", input_key="question", output_key='answer', return_messages=True)

# Create a ConversationalRetrievalChain using the LLM, Qdrant vector store, and memory
chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=qdrant.as_retriever(), memory=memory)

# Initialize an empty list to store chat history
chat_history = []

# Define a function for conducting a conversational chat
def conversational_chat(query):
    # Append the current query to the chat history
    chat_history.append(query)
    
    # Combine the current query with the chat history
    combined_input = {"question": query, "chat_history": chat_history}

    # Process the input using the chain object
    result = chain(combined_input)

    # Extract the answer from the result
    return result["answer"]

# Define a route '/ask' for handling POST requests
@app.route('/ask', methods=['POST'])
def ask_question():
    try:
        # Get the user input from the request
        user_input = request.json['user_input']

        # Process the user input using the conversational_chat function
        output = conversational_chat(user_input)

        # Return the result as JSON
        return jsonify({"response": output})

    except Exception as e:
        # Return an error message if an exception occurs
        return jsonify({"error": str(e)}), 400

# Run the Flask application if the script is executed
if __name__ == '__main__':
    app.run(debug=True)
