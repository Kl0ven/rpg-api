# RPG-API, Simple API to play RPG ⚔


This API is a Lootbox/RPG mini game meant to be used for a discord bot.

## 0.1.0
Upon request if a user is not found in DB then it will be created. 
User have money and lootboxes to start. They can open lootboxes for money.
As you migth have guess, lootboxes lot items (Blade, Potion, Hammer, Axe, Armor)
Each item has a rarety factor and a small image generated procedurally using the  [RPG icon generator](https://github.com/Kl0ven/rpg-icon-generator) module

### Images example
![Blade_0](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/blades/blade_0.png)![Potion_0](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/potions/potion_0.png)![Axe_0](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/axes/axe_0.png)![Armor_0](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/armors/armor_0.png)![Hammer_0](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/hammers/hammer_0.png)
![Blade_41](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/blades/blade_41.png)![Potion_41](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/potions/potion_41.png)![Axe_41](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/axes/axe_41.png)![Armor_41](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/armors/armor_41.png)![Hammer_41](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/hammers/hammer_41.png)
![Blade_61](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/blades/blade_61.png)![Potion_61](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/potions/potion_61.png)![Axe_61](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/axes/axe_61.png)![Armor_61](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/armors/armor_61.png)![Hammer_61](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/hammers/hammer_61.png)
![Blade_85](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/blades/blade_85.png)![Potion_85](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/potions/potion_85.png)![Axe_85](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/axes/axe_85.png)![Armor_85](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/armors/armor_85.png)![Hammer_85](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/hammers/hammer_85.png)
![Blade_100](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/blades/blade_100.png)![Potion_100](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/potions/potion_100.png)![Axe_100](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/axes/axe_100.png)![Armor_100](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/armors/armor_100.png)![Hammer_100](https://raw.githubusercontent.com/Kl0ven/rpg-icon-generator/master/docs/hammers/hammer_100.png)


## 0.2.0
You now have access to your hero with health, and selected items (1 armor, 1 weapon, N potions).
You can select items with  select_loot/ and unselect with unselect_loot/.

With all your selected loots, you can go crawl a dungeon (with other user if you want). 
The dungeon is compose of multiple room with increasing difficulty.
Crawling dungeon is long ;)
Potion is a one use item, it will be gone if it's use in the dungeon.
After the dungon (can take a while IRL) you will be able to see a battle report.
Opening this battle report wil give you lootboxes and money; You can also access a full report.
A Full report is a turn by turn report on your run.
You can also see all the other user and their status (Idle, Crawling Dungeon) to organise a Raid.
When Idling you will regain health.

### Full report example
```
Kloven, Haukain: Entering dungeon
Kloven, Haukain: Enter room 1
In the room there is:
##################################################
Zombie1: (health: 16, atk: 10, def: 7, crit: 10%)
##################################################
Room_1: Rolling initiative...
##################################################
Haukain: Rolled 44 in initiative (1d100)
Zombie1: Rolled 39 in initiative (1d100)
Kloven: Rolled 22 in initiative (1d100)
##################################################
Room_1: Start of turn 1
######################################################################
Haukain: Start his turn 1
Haukain: (health: 100, atk: 0, def: 0, crit: 10%)
Haukain: Choose to Attack Zombie1
Haukain: Roll a 16
Haukain: Hit Zombie1 with 0 DMG
####################
Zombie1: Start his turn 1
...
```

## Swagger
Check out the [swagger-UI](https://kl0ven.github.io/rpg-api/) to see every endpoint


## Run 
```
docker run -d  -p 8080:8080 -e DATABASE_URL=postgresql://postgres:start@db:5432/rpg_api kloven/rpg-api:0.0.1
```
 - -p Expose port 8080
 - -e Pass your database connection string as an environement variable

## Configuration 
With docker compose you can mount a volume in /usr/src/app/config and create a config.py file in that directory.

The config file should look something like this
```python
CONFIG = {
    "start_money" : 500,
    "start_lootboxes": 3,
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
    },
    # max hero health
    "max_health": 100,

    # 0.5 hp / min
    "natural_regen_rate": 0.5,

    # 0 => constant fleeing
    # 1 => no fleeing
    "fleeing_chance": 0.999,

    # all mob possible
    "mobs": [
        {
            "name": "zombie",
            "atk": (1, 30),
            "def": (0, 23),
            "health": (10, 45)
        },
        {
            "name": "dragon",
            "atk": (20, 50),
            "def": (50, 85),
            "health": (15, 300)
        },
        {
            "name": "witch",
            "atk": (15, 40),
            "def": (0, 56),
            "health": (10, 50)
        },
        {
            "name": "skeleton",
            "atk": (2, 35),
            "def": (0, 25),
            "health": (2, 34)
        },
        {
            "name": "slime",
            "atk": (2, 30),
            "def": (10, 45),
            "health": (2, 50)
        },
        {
            "name": "wearwolf",
            "atk": (2, 47),
            "def": (10, 45),
            "health": (2, 80)
        }
    ],

    #every "mob_increment" romms the number of mob goes up by one
    "mob_increment": 10,

    # chance of player taking a potion if it has one
    "potion_chance": 0.2,

    # crit on 1d100 
    # here crit if 1d100 > 90 
    "crit": 10,

    # crit multiplier 
    "crit_power": 1.6,

    # potion effects
    "effects_power": {
        # add 50% atk 
        "strength": 0.5,
        # add 50% atk
        "protection": 0.5,
        # give btween 20 and 50 health
        "health": (20, 50),
        # add from 10 to 60 to crit 
        "agility": (10, 50),
        # regain 5-30 health per turn
        "regeneration": (5, 30)
    },
    # (min, max) in number of turn 
    "effects_duration": {
        "common": (1, 2),
        "uncommon": (2, 3),
        "rare": (2, 4),
        "epic": (3, 4),
        "outstanding": (3, 5)
    },

    # balancing act
    # systematic regen btw room
    "btw_rooms_regen": 30,

    # set the time your hero will be away
    "minutes_per_room": 10,

    # money = sum(1,2,3, ...nb_room_clear) * money_coef
    "money_coef" : 100,

    "lootboxes_rarety_by_rooms_range": [
        {"rarety": 0, "range": (0, 9), "nb_lootboxes": (1, 2)},
        {"rarety": 1, "range": (10, 19), "nb_lootboxes": (1, 2)},
        {"rarety": 2, "range": (20, 29), "nb_lootboxes": (1, 3)},
        {"rarety": 3, "range": (30, 39), "nb_lootboxes": (2, 3)},
        {"rarety": 4, "range": (40, 999999), "nb_lootboxes": (2, 4)},
    ],
}

```

## Persistance:
You should also mount a volume to persiste data (items images, and battle reports):
```yaml
volumes:
      - ./.assets:/usr/src/app/assets

```