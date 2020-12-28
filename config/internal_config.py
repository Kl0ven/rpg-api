from rpg_icon_generator import Blade_Generator, Potion_Generator, Axe_Generator, Armor_Generator, Hammer_Generator
import os

RARETY = {
    "common": 0,
    "uncommon": 1,
    "rare": 2,
    "epic": 3,
    "outstanding": 4
}


LOOT_TYPE = {
    "blade": 0,
    "potion": 1,
    "axe": 2,
    "armor": 3,
    "hammer": 4
}

LOOT_GENERATOR = {
    "blade": Blade_Generator,
    "potion": Potion_Generator,
    "axe": Axe_Generator,
    "armor": Armor_Generator,
    "hammer": Hammer_Generator
}

COMPLEXITY_RANGE = {
    "common": (0, 40),
    "uncommon": (41, 60),
    "rare": (61, 85),
    "epic": (86, 95),
    "outstanding": (96, 100)
}



INTERNAL_CONFIG = {
    "lootboxes_rarety": RARETY,
    "invert_lootboxes_rarety": {v: k for k, v in RARETY.items()},
    "loot_type": LOOT_TYPE,
    "invert_loot_type": {v: k for k, v in LOOT_TYPE.items()},
    "rarety": list(RARETY.keys()),
    "complexity_range": COMPLEXITY_RANGE,
    "loot_type" : LOOT_TYPE,
    "loot_generator": LOOT_GENERATOR,
    "image_dimension": 64,
    "image_render_scale": 2,
    "image_output_directory": os.path.normpath(os.path.join(os.getcwd(), "images/"))
}
