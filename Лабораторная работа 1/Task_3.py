players=['player_1','player_2','player_3','player_4','player_5','player_6']
summa=len(players)
players_in_team =summa//2
team_1=players[0:players_in_team]
team_2=players[players_in_team:]
print(team_1,team_2)
