import requests
from bs4 import BeautifulSoup

def github_search(query):
    url = f"https://github.com/search?q={query}&type=repositories"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Send GET request to GitHub
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch data from GitHub. Status code: {response.status_code}")
        return []

    # Parse HTML response
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all repository links
    repo_links = soup.find_all("a", class_="v-align-middle")

    # Extract repository names and URLs
    repos = []
    for link in repo_links:
        repo_name = link.text.strip()
        repo_url = "https://github.com" + link["href"]
        repos.append({"name": repo_name, "url": repo_url})

    return repos

if __name__ == "__main__":
    search_query = input("Enter search query: ")
    results = github_search(search_query)
    print("\nSearch Results:")
    for result in results:

        print(f"{result['name']}: {result['url']}")

