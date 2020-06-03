# lol_15ff_model
To provide an API that determines whether a player should surrender or not to save time.
## Model 
Uses SGD\
15 min: ~76%\
20 min: ~80%\
Main reason for high accuracy is that most games are landslide wins/losses.\
When team_kills + team_assists < 10, accuracy drops to ~68%\
Features used in current model:
```
  'team_kda_diff',
  'team_cs_diff',
  'team_level_diff',
  'turrets_diff',
  'inhibitors_diff',
  'monsters_diff',
```
## End Points
Production site: https://lol-15ff-model.herokuapp.com/
### api/15 or api/20
POST Request
```
{
  "100": {
      "turrets": "int",
      "herald": "int",
      "baron": "int",
      "dragon": "int",
      "inhib": "int",
      "level": "int",
      "kills": "int",
      "deaths": "int",
      "assists": "int",
      "cs": "int"
  },
  "200": {
      "turrets": "int",
      "herald": "int",
      "baron": "int",
      "dragon": "int",
      "inhib": "int",
      "level": "int",
      "kills": "int",
      "deaths": "int",
      "assists": "int",
      "cs": "int"
  }
}
```
POST Response (success)
```
{
  "msg": { "winningTeam": "100" },
  "status": "ok"
}
```
POST Response (error)
```
{
  "msg": "str",
  "status": "error"
}
```
## Challenges
- Available game features are very correlated: More kills -> More CS, turrets, monsters
- Some games are impossible to predict. Etc big throws
- Some games are difficult to predict. Etc both team are performing very close and there is no clear distinction which team has the advantage
## Model Attempts
### Attempt 1
Method: Use each player's kda as features, etc player_1_kills, player_1_deaths...\
Result: Does work, but not as good as consolidating into team kills
### Attempt 2
Method: Use player's roles as features, etc TOP_SOLO_TEAM_100_kills, TOP_SOLO_TEAM_100_deaths...\
Result: Similar to Attempt 1
### Attempt 3
Method: Add concept of early/late game champions. 
```
delta = top_champion_win_rate_after_30_min - top_champion_win_rate_before_25_min
```
delta as feature, as scaling for kda, or threshold for multiplier\
Result: All worse than just using consolidated team kda
