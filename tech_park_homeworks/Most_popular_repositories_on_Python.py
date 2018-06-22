import requests

API_URL = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'

def get_most_starred_github_repositories():
        response = requests.get(API_URL)

        if response.status_code == 200:
            return response.json()['items'][:10]

        return


for repo in get_most_starred_github_repositories():
        print(repo['name'])

