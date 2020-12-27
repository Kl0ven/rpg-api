import connexion
import six
from flask import g
import logging

from rpg_api.swagger_models.inventory import Inventory  # noqa: E501
from rpg_api.swagger_models.lootbox_rarety import LootboxRarety
from rpg_api.swagger_models.lootbox import Lootbox as Lootbox_swagger
from rpg_api.swagger_models.loot import Loot as Loot_swagger
from rpg_api import util

from rpg_api.models.lootbox import Lootbox
from rpg_api.models.loot import Loot
from config import CONFIG

logger = logging.getLogger('RPG_API.inventory_controler')

def get_inventory(user):  # noqa: E501
    """Get inventroy information for a specific user

    Return the inventory of a specific user   # noqa: E501

    :param user: the username of the user
    :type user: str

    :rtype: Inventory
    """
    inv = g.user.inventory[0]
    items = []
    lootboxes = Lootbox.select().where(inv.id == Lootbox.inventory)
    for lb in lootboxes:
        lbr = LootboxRarety(value=lb.rarety, name=CONFIG["invert_lootboxes_rarety"][lb.rarety])
        items.append(Lootbox_swagger(name=lb.name, price=CONFIG['lootbox_price'][lbr.name], slot=lb.slot, rarety=lbr))

    loots = Loot.select().where(inv.id == Loot.inventory)
    for l in loots:
        lbt = LootboxRarety(value=l.type, name=CONFIG["invert_loot_type"][l.type])
        items.append(Loot_swagger(name=l.name, slot=l.slot, type=lbt, image_url=l.image_url))
    return items
