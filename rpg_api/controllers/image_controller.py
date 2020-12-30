import connexion
import six
from flask import g
from rpg_api import util
import logging
from os import path
from flask import abort, send_file
from rpg_api.models.loot import Loot
from config import CONFIG

logger = logging.getLogger('RPG_API.image_controler')

def get_image(user, slot):  # noqa: E501
    """Get Image for a specific loot (slot) for a user

    Return Image for a specific loot (slot) for a user  # noqa: E501

    :param user: the username of the user
    :type user: str
    :param slot: the slot of the loot
    :type slot: str

    :rtype: str
    """
    inv = g.user.inventory[0]
    loot = None
    query = Loot.select().where(inv.id == Loot.inventory, Loot.slot == slot)
    if query.exists():
        loot = query.get()
    else:
        abort(404)

    return send_file(path.join(CONFIG["image_output_directory"], loot.image_url))
