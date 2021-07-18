#looping through a list
teamA = ['Marcus', 'david', 'luke']
teamB = ['kevin', 'riyad', 'kun']
teams = [teamA,teamB]

for team in teams:
    for player in team:
        print(player)

for team in teams:
    for m in team:
        print('you are welcome ' + m)


