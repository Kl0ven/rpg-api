import connexion
import six
import random
from flask import g
from playhouse.flask_utils import get_object_or_404
import logging
from config import CONFIG
from rpg_api.swagger_models.inventory import Inventory  # noqa: E501
from rpg_api import util
from rpg_api.models import database
from rpg_api.models.lootbox import Lootbox
logger = logging.getLogger('RPG_API.inventory_controler')

def open_lootbox(user, slot):  # noqa: E501
    """Open lootbox from user wich is at slot

    Open the lootbox from user wich is at slot in inventory  # noqa: E501

    :param user: the username of the user
    :type user: str
    :param slot: the slot of the lootbox
    :type slot: int

    :rtype: Inventory
    """
    with database.database.atomic():
        inv = g.user.inventory[0]
        lootbox = get_object_or_404(Lootbox.select().where(inv.id == Lootbox.inventory), Lootbox.slot == slot)
        lootbox_rarety_name = lootbox.get_rarety_name()
        loot_range = CONFIG["lootbox_size_range"][lootbox_rarety_name]
        for i in range(random.randrange(*loot_range)):
            loot_rarety = random.choices(
                CONFIG["rarety"], 
                CONFIG["lookup_table_lootbox_loot_distribution"][lootbox_rarety_name],
                k=1)
            loot_complexity = random.randrange(*CONFIG["complexity_range"][loot_rarety[0]])
            loot_type = random.choice(list(CONFIG["loot_type"].keys()))
            loot_generator = CONFIG['loot_generator'][loot_type]
    return {"loot_rarety": loot_rarety, "loot_complexity": loot_complexity, "loot_type": loot_type}
