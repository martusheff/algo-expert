competitions = [
    ["AlgoMasters", "FrontPage Freebirds"],
    ["Runtime Terror", "Static Startup"],
    ["WeC#", "Hypertext Assassins"],
    ["AlgoMasters", "WeC#"],
    ["Static Startup", "Hypertext Assassins"],
    ["Runtime Terror", "FrontPage Freebirds"],
    ["AlgoMasters", "Runtime Terror"],
    ["Hypertext Assassins", "FrontPage Freebirds"],
    ["Static Startup", "WeC#"],
    ["AlgoMasters", "Static Startup"],
    ["FrontPage Freebirds", "WeC#"],
    ["Hypertext Assassins", "Runtime Terror"],
    ["AlgoMasters", "Hypertext Assassins"],
    ["WeC#", "Runtime Terror"],
    ["FrontPage Freebirds", "Static Startup"]
  ]
results = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]



def tournamentWinner(competitions, results):
    # Write your code here.\
    teamNames = []
    teams = {}

    for i in range(len(competitions)):
        for j in range(len(competitions[i])):
            if j not in teamNames:
                teamNames.append(competitions[i][j])

    team = set(teamNames)

    for i in team:
        newTeam = {i: 0}
        teams.update(newTeam)

    for i in range(len(competitions)):

        if results[i] == 1:
            teams[competitions[i][0]] += 3
        elif results[i] == 0:
            teams[competitions[i][1]] += 3

    highScore = 0
    winningTeam = ""
    for key, value in teams.items():
        if value > highScore:
            highScore = value
            winningTeam = key


    return winningTeam












def main():
    tournamentWinner(competitions, results)

if __name__ == "__main__":
    main()