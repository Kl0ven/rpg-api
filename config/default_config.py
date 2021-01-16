DEFAULT_CONFIG = {
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

    # 0 => constant fleeing
    # 1 => no fleeing
    "fleeing_chance": 0.999,

    # all mob possible
    "mobs": [
        {
            "name": "zombie",
            "atk": (1, 56),
            "def": (0, 23),
            "health": (10, 45)
        },
        {
            "name": "dragon",
            "atk": (20, 80),
            "def": (50, 85),
            "health": (15, 300)
        },
        {
            "name": "witch",
            "atk": (15, 75),
            "def": (0, 56),
            "health": (10, 50)
        },
        {
            "name": "skeleton",
            "atk": (2, 75),
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
            "atk": (2, 50),
            "def": (10, 45),
            "health": (2, 80)
        }
    ],

    #every "mob_increment" romms the number of mob goes up by one
    "mob_increment": 10,

    # chance of player taking a potion if it has one
    "potion_chance": 0.2,

    # crit starting point on 1d100 
    # here crit if 1d100 > 90 
    "crit": 90,

    # crit multiplier 
    "crit_power": 1.6
}
