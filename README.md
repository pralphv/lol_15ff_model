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
