LOOTBOXES_RARETY = {
    "common": 0,
    "uncommon": 1,
    "rare": 2,
    "epic": 3,
    "outstanding": 4
}


LOOT_TYPE = {
    "potion": 0,
    "test": 1,
    "test2": 2,
    "couocu": 3
}



INTERNAL_CONFIG = {
    "lootboxes_rarety": LOOTBOXES_RARETY,
    "invert_lootboxes_rarety": {v: k for k, v in LOOTBOXES_RARETY.items()},
    "loot_type": LOOT_TYPE,
    "invert_loot_type": {v: k for k, v in LOOT_TYPE.items()},
}
