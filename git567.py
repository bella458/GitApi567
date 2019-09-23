"""Bella Manoim 

   Git API assignment
   
   Requirements:
   Write a function that will take as input a GitHub user ID. 
   The output from the function will be a list of the names of the 
   repositories that the user has, along with the number of commits 
   that are in each of the listed repositories.
   
   Note- I commented out some lines I used for testing my code
"""

import requests
import json


def getRepositories(username):
    repositoriesResponse = requests.get("https://api.github.com/users/" + username + "/repos")   
    repositories = json.loads(repositoriesResponse.text)
    """print (repositories)"""
    repositorylist = []
    
    for repository in repositories:
        repositorylist.append(repository.get("name"))
        """print (repositorylist)"""
    return repositorylist

def getCommits(username, repositoryName):
    commitsResponse = requests.get("https://api.github.com/repos/" + username + "/" + repositoryName + "/commits")   
    commitsText = json.loads(commitsResponse.text)
    """print(commitsText)"""
    commits = len(commitsText)
    """print (commits)"""
    return (commits)

def main():
    commitResult = getRepositories("bella458")

    for repository in commitResult:
        commits = getCommits("bella458",repository)
        print("Repository: " + repository + " Commits: " + str((commits)))


if __name__ == "__main__":
    main()