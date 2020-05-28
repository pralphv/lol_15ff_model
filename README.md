# lol_15ff_model
### api/15
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
Result: All worse than just using consolidating team kda
