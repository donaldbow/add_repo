import requests

def create_github_repo(repo_name, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    data = {
        'name': repo_name,
        'auto_init': True  # Create an initial commit
    }

    try:
        response = requests.post('https://api.github.com/user/repos', json=data, headers=headers)

        if response.status_code == 201:
            print(f"Repository '{repo_name}' created successfully!")
        else:
            print(f"Failed to create repository. Status code: {response.status_code}")
            print(response.json())

    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_ACCESS_TOKEN' with your actual GitHub access token
    access_token = 'YOUR_ACCESS_TOKEN'
    
    # Replace 'NewRepo' with the desired repository name
    repo_name = 'NewRepo'

    create_github_repo(repo_name, access_token)
