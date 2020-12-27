import connexion
import six
from flask import g
import logging

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
        items.append(lb)

    loots = Loot.select().where(inv.id == Loot.inventory)
    for l in loots:
        items.append(l)
        
    return items
