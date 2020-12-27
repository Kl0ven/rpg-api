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
    }
}
