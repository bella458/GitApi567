"""Bella Manoim 
   

"""

import requests
import json


def getRepositories(username):
    repositoriesResponse = requests.get("https://api.github.com/users/" + username + "/repos")   
    repositories = json.loads(repositoriesResponse.text)
    repositorylist = []
    
    for repository in repositories:
        repositorylist.append(repository.get("name"))
    return repositorylist

def getCommits(username, repositoryName):
    commitsResponse = requests.get("https://api.github.com/repos/" + username + "/" + repositoryName + "/commits")   
    commitsText = json.loads(commitsResponse.text)
    commits = len(commitsText)
    return (commits)

def main():
    commitResult = getRepositories("bella458")

    for repository in commitResult:
        commits = getCommits("bella458",repository)
        print("Repository: " + repository + " Commits: " + str((commits)))


if __name__ == "__main__":
    main()