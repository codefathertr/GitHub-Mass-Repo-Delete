import requests

# Gerekli bilgileri gir
GITHUB_USERNAME = "codefathertr"  # Your username - Kullanıcı adınızı girin.

#  https://github.com/settings/tokens buradan oluşturun / creating api tokens

GITHUB_TOKEN = "ghp_..."  # Personal Access Token 



# Tüm repoları çek
def get_repos():
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/user/repos?per_page=100&page={page}"
        response = requests.get(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

# Repoları sil
def delete_repo(repo_name):
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}"
    response = requests.delete(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    if response.status_code == 204:
        print(f"[+] Silindi: {repo_name}")
    else:
        print(f"[-] Silinemedi: {repo_name} | Status: {response.status_code}")

def main():
    repos = get_repos()
    print(f"{len(repos)} repo bulundu.")
    onay = input("Tüm repoları silmek istediğine emin misin? (evet/hayır): ")
    if onay.lower() != "evet":
        return

    for repo in repos:
        delete_repo(repo["name"])

if __name__ == "__main__":
    main()
