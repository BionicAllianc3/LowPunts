homexG = [0.32, 0.73, 0.11, 0.32, 0.59, 0.34, 0.25]
awayxG = [0.45, 0.66, 0.12, 0.42, 0.67, 0.22, 0.80]

import random
def calculatewinner(home,away):
    homegoals = 0
    awaygoals = 0

    def testshots(shots):
        Goals = 0
        for shot in shots:
            if random.random()<=shot:
                Goals+=1
        return Goals

    homegoals = testshots(home)
    awaygoals = testshots(away)

    if homegoals>awaygoals:
        return ("home")
    elif homegoals<awaygoals:
        return ("away")
    else:
        return ("draw")

def calculateChance(team1, team2):
    home = 0;
    away = 0;
    draw = 0;

    for i in range(0, 10000):
        matchwinner = calculatewinner(team1,team2)
        if matchwinner == "home":
            home+=1
        elif matchwinner == "away":
            away+=1
        else:
            draw+=1

    home = home/100
    away = away/100
    draw = draw/100
    print(f' Over 10,000 games, home wins {home}%, away wins {away}% and draw in {draw}% of the games')
calculateChance(homexG,awayxG)