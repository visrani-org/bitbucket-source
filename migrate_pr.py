import requests

# Bitbucket API credentials
BITBUCKET_USERNAME = 'BCdqaZKV8EeShxCBPP'
BITBUCKET_APP_PASSWORD = 'sAtjVmfUvnC6pswhwmG5fxHm7CpkfsDT'
BITBUCKET_TOKEN = 'ATCTT3xFfGN0-BS47x58CextR9AOC9hYgPsmZ5ppXxNEDZWe0J3n0phYw7m9KknlGCPccEZBbAp8FOlM6-P886pu7oOjiWpiypDv42CwFcDrxACoTJImKztPArMUKHGM5EBy1brQGxWPdTBVbfsTk-yBVEwdKhb2P01GxVoLIByLFZWy7QQE4ag=7E0CB0B6'

# GitHub API credentials
GITHUB_USERNAME = 'visrani'
GITHUB_TOKEN = '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'

# Bitbucket repository information
BITBUCKET_OWNER = 'visrani-playground'
BITBUCKET_REPO = 'integrate-github'

# GitHub repository information
GITHUB_OWNER = 'visrani'
GITHUB_REPO = 'bitbucket-source'

# Bitbucket API endpoint to fetch pull requests
BITBUCKET_API_ENDPOINT = f'https://api.bitbucket.org/2.0/repositories/{BITBUCKET_OWNER}/{BITBUCKET_REPO}/pullrequests'

# GitHub API endpoint to create pull requests
GITHUB_API_ENDPOINT = f'https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/pulls'


# Fetch pull requests from Bitbucket
def get_bitbucket_pull_requests():
    #url = f'{BITBUCKET_API_ENDPOINT}?state=OPEN'
    url = BITBUCKET_API_ENDPOINT
    headers = {
        'Authorization': f'Bearer {BITBUCKET_TOKEN}',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    print(url)
    print(response.json()['values'])
    return response.json()['values']


# Create pull request in GitHub
def create_github_pull_request(pull_request):
    data = {
        'title': pull_request['title'],
        'body': pull_request['description'],
        'head': f'{BITBUCKET_OWNER}:{pull_request["source"]["branch"]["name"]}',
        'base': 'main'  # Change to your target branch in GitHub
    }
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.post(GITHUB_API_ENDPOINT, json=data, headers=headers)
    return response.json()


# Main script
if __name__ == '__main__':
    # Fetch pull requests from Bitbucket
    pull_requests = get_bitbucket_pull_requests()

    # Create pull requests in GitHub
    for pull_request in pull_requests:
        response = create_github_pull_request(pull_request)
        print(f'Pull request created in GitHub: {response["html_url"]}')
