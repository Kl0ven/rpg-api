import connexion
import six
from flask import g, abort
from rpg_api import util
import logging
from rpg_api.models import database
from rpg_api.models.loot import Loot
from playhouse.flask_utils import get_object_or_404
from config import CONFIG
logger = logging.getLogger('RPG_API.selection_controler')


def select_loot(body, user):  # noqa: E501
    """Select Loot from user wich is at slot

    select the Loot(s) from user wich is at slot in inventory  # noqa: E501

    :param body: the slot(s) of the loot(s)
    :type body: List[]
    :param user: the username of the user
    :type user: str

    :rtype: None
    """
    loots = []
    inv = g.user.inventory[0]
    with database.database.atomic() as ctx:
        for slot in body:
            loots.append(get_object_or_404(Loot.select().where(inv.id == Loot.inventory), Loot.slot == slot))

        res, exp = check_selection(loots)
        if not res:
            ctx.rollback()
            abort(412, exp)
        
        for l in loots:
            if l.type == CONFIG["loot_type"]["armor"]:
                query_old = Loot.select().where(inv.id == Loot.inventory, Loot.type == CONFIG["loot_type"]["armor"], Loot.selected == True)
                for old in query_old:
                    old.selected = False
                    old.save()
                l.selected = True
                l.save()
            elif l.type in CONFIG["weapon"]:
                query_old = Loot.select().where(inv.id == Loot.inventory, Loot.type << CONFIG["weapon"], Loot.selected == True)
                for old in query_old:
                    old.selected = False
                    old.save()
                l.selected = True
                l.save()
            else:
                l.selected = True
                l.save()
    return None, 200


def unselect_loot(body, user):  # noqa: E501
    """UnSelect Loot from user wich is at slot

    unselect the Loot(s) from user wich is at slot in inventory  # noqa: E501

    :param body: the slot(s) of the loot(s)
    :type body: List[]
    :param user: the username of the user
    :type user: str

    :rtype: None
    """
    inv = g.user.inventory[0]
    with database.database.atomic() as ctx:
        for slot in body:
            loot = get_object_or_404(Loot.select().where(inv.id == Loot.inventory), Loot.slot == slot)
            loot.selected = False
            loot.save()
    return None, 200

def check_selection(loots):
    armor = len(list(filter(lambda l: l.type == CONFIG["loot_type"]["armor"], loots)))
    weapon = len(list(filter(lambda l: l.type in CONFIG["weapon"], loots)))
    res = (True, "")
    if armor > 1:
        res = (False, "Only one armor can be selected")
    if weapon > 1:
        res = (False, "Only one weapon can be selected")
    return res
