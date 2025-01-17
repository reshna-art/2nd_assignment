#Simple GET Request: Use the requests library to fetch data from an API (e.g., JSONPlaceholder) and display the titles of the first 5 posts

import requests

# URL of the public API
url = "https://jsonplaceholder.typicode.com/posts"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Data fetched successfully!\n")
    # Parse the JSON data
    data = response.json()

    # Display the first 5 posts
    for post in data[:5]:
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")