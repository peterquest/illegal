# Daily updates for futures bet 2025
# league with batman, spender, warren, curto, and me

# pq 3/25/2025
# let's actually finish this.

## TO DO:
##   DONE. update team info for 2025
##   DONE. correctly evaluate rules: top 2!
##   2. clean up formatting of print() output
##   3. tracker/countdown for all bets
##   4. include draft position next to player listings
##

import logging
import datetime
import statsapi as mlb

'''
ALL TEAM IDS:

    Oakland Athletics 133
    Pittsburgh Pirates 134
    San Diego Padres 135
    Seattle Mariners 136
    San Francisco Giants 137
    St. Louis Cardinals 138
    Tampa Bay Rays 139
    Texas Rangers 140
    Toronto Blue Jays 141
    Minnesota Twins 142
    Philadelphia Phillies 143
    Atlanta Braves 144
    Chicago White Sox 145
    Miami Marlins 146
    New York Yankees 147
    Milwaukee Brewers 158
    Los Angeles Angels 108
    Arizona Diamondbacks 109
    Baltimore Orioles 110
    Boston Red Sox 111
    Chicago Cubs 112
    Cincinnati Reds 113
    Cleveland Guardians 114
    Colorado Rockies 115
    Detroit Tigers 116
    Houston Astros 117
    Kansas City Royals 118
    Los Angeles Dodgers 119
    Washington Nationals 120
    New York Mets 121
'''


# each squad is a dict of 3 lists of lists which contain
# for team wins: [team_name, team_id, win_total]
# for homers and wins: [player, player_id, stat_total]
# pitcherwins and homers use player_id's to ensure uniquity. we just append the relevant
# stat to each of these lists via the loops below where we poll current data. then use the
# squad dicts to generate output.

'''
PETES SQUADS
'''

pete = {} 
# Phillies, Orioles, DBacks, Royals, Guardians
pete["teamwins"] = [["Phillies", 143],["Orioles", 110],["DBacks", 109],["Royals", 118],["Guardians", 114]]
# Wheeler, Skenes, Webb, Snell
pete["pitcherwins"] = [["Wheeler", 554430],["Skenes", 694973],["Webb", 657277],["Snell", 605483]]
# Judge, Tatis, Riley, Ozuna
pete["homers"] = [["Judge", 592450],["Tatis", 665487],["Riley", 663586],["Ozuna", 542303]]


'''
BATMANS'S SQUADS
'''
# Braves, Mariners, Cubs, Jays, Cards
# Skubal, Sasaki, Ragans, Nola
# Rooker, Schwarbs, JRam, Trout

batman = {} 
batman["teamwins"] = [["Braves", 144],["Mariners", 136],["Cubs", 112],["Jays", 141],["Cards", 138]]
batman["pitcherwins"] = [["Skubal", 669373],["Sasaki", 808963],["Ragans", 666142],["Nola", 605400]]
batman["homers"] = [["Rooker", 667670],["Schwarbs", 656941],["JRam", 608070],["Trout", 545361]] 

'''
CUETO'S SQUADS
'''
# Red Sox, Yankees, Brewers, Tigers, Athletics
# Burnes, Gilbert, Yamamoto, Schwellenbach
# Ohtani, Olson, Witt, Harper

cueto = {} 
cueto["teamwins"] = [["Red Sox", 111],["Yankees", 147],["Brewers", 158],["Tigers", 116],["Athletics", 133]]
cueto["pitcherwins"] = [["Burnes", 669203],["Gilbert", 669302],["Yamamoto", 808967],["Schwellenbach", 680885]]
cueto["homers"] = [["Ohtani", 660271],["Olson", 621566],["Witt", 677951],["Harper", 547180]]

'''
WARREN'S SQUADS
'''
# Mets, Rangers, Padres, Reds, Nationals
# Sale, Fried, Brown, Miller
# Soto, Santander, Vlad, Vientos

warren = {} 
warren["teamwins"] = [["Mets", 121],["Rangers", 140],["Padres", 135],["Reds", 113],["Nationals", 120]]
warren["pitcherwins"] = [["Sale", 519242],["Fried", 670770],["Brown", 686613],["Miller", 682243]]
warren["homers"] = [["Soto", 665742],["Santander", 623993],["Vlad Jr.", 665489],["Vientos", 668901]]

'''
SPENDER'S SQUADS
'''
# Dodgers, Astros, Twins, Rays, Giants
# Valdez, Castillo, Cease, Crochet
# Yordan, Alonso, Devers, Henderson

spender = {} 
spender ["teamwins"] = [["Dodgers", 119],["Asstros", 117],["Twins", 142],["Rays", 139],["Giants", 137]]
spender ["pitcherwins"] = [["Valdez", 664285],["Castillo", 622491],["Cease", 656302],["Crochet", 676979]]
spender ["homers"] = [["Yordan", 670541],["Alonso", 624413],["Devers", 646240]]#,["Henderson", 683002]] gunnar needs to play a game

players = [pete, batman, cueto, warren, spender]
playernames = ["PETE", "BATMAN", "CUETO", "WARREN", "SPENDER"]
standings = mlb.standings_data(leagueId="103,104", division="all", include_wildcard=False, season=None, standingsTypes=None, date=None)

# for each team in totals list, get their current w-l, pace, and compare to total





#build our own wintotals list.
#do this to just simplify the references to wins/losses
#should look like [(name, id, w, l)]

winloss = []
#check each division
for i in range(6):
     #check each team
  for j in range(5):
   team_id = standings[200+i]['teams'][j]['team_id']
   teamname   = standings[200+i]['teams'][j]['name']
   teamwins   = standings[200+i]['teams'][j]['w']
   teamlosses = standings[200+i]['teams'][j]['l']
   winloss.append((teamname, teamwins, teamlosses, team_id))

#   teampace   = str(round((teamwins / (teamwins+teamlosses)) * 162.0, 2))
#   line       = totals[team_id]['line']
#   print(totals[team_id]['team'])
#   print(teamname, teamwins, '-', teamlosses, 'pace:', teampace, 'line:', totals[team_id]['ou'],line)

#stupid html formatting for now
print("<pre>")

'''
loops
'''

for i in range(2):
 playername = playernames[i]
 print("-- " + playername + " HOMERS --")
# tot = 0
 for x in players[i]['homers']:
  print(x[0])
  num = mlb.player_stat_data(x[1],'hitting','season')['stats'][0]['stats']['homeRuns']
  x.append(num)
  print(num)
 # tot += num  DO THIS LATER
 

 players[i]['homers']= sorted(players[i]['homers'], key=lambda i: i[2], reverse=True)
 tot=players[i]['homers'][0][2]+players[i]['homers'][1][2]
 print(players[i]['homers'][0:2])
 print("<s>", players[i]['homers'][2:], "</s>")
 print("total homers:", tot)

 print("-- " + playername + " PITCHER WINS --")
 #tot = 0
 for x in players[i]['pitcherwins']:
  print (x[0])
  num = mlb.player_stat_data(x[1],'pitching','season')['stats'][0]['stats']['wins']
  x.append(num)
  print(num)
#  tot += num

 players[i]['pitcherwins']=sorted(players[i]['pitcherwins'], key=lambda i: i[2],reverse=True)
 tot=players[i]['pitcherwins'][0][2]+players[i]['pitcherwins'][1][2]
 print(players[i]['pitcherwins'][0:2])
 print("<s>", players[i]['pitcherwins'][2:], "</s>")
 print("total pitcher wins:", tot)

#change this so the order follows the draft order established in players[i]['teamwins']
# right now it ends up going by team_id alphanumerically. so iterate across ^^^^ rather than
# across winloss
 print("--", playername, "TEAM WINS --")
 tot=0
 for x in winloss:
  # check team id against list of teams each player owns
  if (x[3] in [z[1] for z in players[i]["teamwins"]]):
   print(x[0], "have", x[1], "wins.")
   tot+=x[1]
 print(tot, "total team wins\n")



'''
# get relevant win total data out of standings in a way that's easier to access by ID
#for i in 6:
# for 

#print('The A\'s won %s games in 2024.' % sum(1 for x in mlb.schedule(team=133,start_date='03/01/2024',end_date='04/08/2024') if (x.get('winning_team','')=='Oakland Athletics') and x.get('game_type','')=='R'))

'''



#stupid html formatting for now
print("</pre>")
