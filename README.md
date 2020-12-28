# RPG-API, Simple API to play RPG ⚔


This API is a Lootbox/RPG mini game meant to be used for a discord bot.

## 0.1.0
Upon request if a user is not found in DB then it will be created. 
User have money and lootboxes to start. They can open lootboxes for money.
As you migth have guess, lootboxes lot items (Blade, Potion, Hammer, Axe, Armor)
Each item has a rarety factor and a small image generated procedurally using the  [RPG icon generator](https://github.com/Kl0ven/rpg-icon-generator) module

## 0.2.0
WIP :)

## Swagger
Check out the [swagger-UI](https://kl0ven.github.io/rpg-api/) to see every endpoint


## Run 
```
docker run -d  -p 8080:8080 -e DATABASE_URL=postgresql://postgres:start@db:5432/rpg_api kloven/rpg-api:0.0.1
```
 - -p expose port 8080
 - -e Pass your database connection string as an environement variable

## Configuration 
With docker compose you can mount a volume in /usr/src/app/config and create a config.py file in that directory.

The config file should look something like this
```python
CONFIG = {
    # the money every user start with
    "start_money" : 500,
    # the number of loot boxes every user start with
    "start_lootboxes": 3,
    # the lootbox price by rarety
    "lootbox_price": {
        "common": 100,
        "uncommon": 300,
        "rare": 500,
        "epic": 800,
        "outstanding": 1000
    },
    # for each lootbox rarety define number of loot it contain as a range (min, max)
    "lootbox_size_range": {
        "common": (1, 3),
        "uncommon": (2, 3),
        "rare": (2, 4),
        "epic": (2, 4),
        "outstanding": (2, 5)
    },
    # for each lootbox rarety define the distribution of the loot rarety [common, uncommon, rare, epic, outstanding]
    # sum of the distribution array must be 1
    "lookup_table_lootbox_loot_distribution": {
        "common": [0.9, 0.1, 0, 0, 0],
        "uncommon": [0.2, 0.7, 0.1, 0, 0],
        "rare": [0.1, 0.1, 0.7, 0.1, 0],
        "epic": [0.05, 0.05, 0.1, 0.7, 0.1],
        "outstanding": [0.05, 0.05, 0.05, 0.2, 0.65]
    }
}
```