import requests

def display_welcome():
    print("=== Welcome to the Conversational Retrieval System ===")
    print("This script interacts with a Flask API for contextual answers.")
    print("Enter your query, and the system will provide a response.\n")

def test_flask_api():
    # Update the URL based on your Flask app's configuration
    api_url = "http://localhost:5000/ask"

    # Sample user input
    user_input = input("Enter your query: ")

    # Prepares the payload
    payload = {"user_input": user_input}

    try:
        # Send the POST request
        response = requests.post(api_url, json=payload)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response content
            print("\nSystem Response:")
            print("-----------------")
            print("Response:", response.json()['response'])
        else:
            print(f"Error: {response.status_code}\n{response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == '__main__':
    display_welcome()
    test_flask_api()
