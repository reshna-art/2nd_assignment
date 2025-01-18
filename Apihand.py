import requests

def fetch_users():
    url = "https://api.github.com/users"
    params = {
        "page": 1,    # Start with the first page
        "per_page": 10  # Fetch 10 users per page
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        users = response.json()
        for user in users:
            print(f"User: {user['login']}, URL: {user['html_url']}")
    else:
        print(f"Failed to retrieve data: {response.status_code}")

# Call the function
fetch_users()

