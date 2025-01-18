import requests

def simulate_post_request():
    """
    Simulate sending a POST request to create a new post on JSONPlaceholder.
    """
    # URL for the JSONPlaceholder API (for real-world scenarios)
    url = "https://jsonplaceholder.typicode.com/posts"

    # Data to send in the POST request
    post_data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    # Simulate the POST request (uncomment the real request in a live environment)
    try:
        # response = requests.post(url, json=post_data)
        # Simulating the expected response
        response = {
            "id": 101,  # JSONPlaceholder usually assigns the next available ID
            "title": post_data["title"],
            "body": post_data["body"],
            "userId": post_data["userId"]
        }
        print("POST request simulated successfully.")
        print("Response:", response)
    except Exception as e:
        print("An error occurred while simulating the POST request:", e)

# Example usage
if __name__ == "__main__":
    simulate_post_request()
