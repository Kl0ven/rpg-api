import connexion
import six
import random
import logging
from os import path
from flask import g
from flask import abort
from datetime import datetime
from coolname import RandomGenerator
from playhouse.flask_utils import get_object_or_404
from coolname.loader import load_config
import hashlib

from config import CONFIG
from rpg_api import util
from rpg_api.models import database
from rpg_api.models.lootbox import Lootbox
from rpg_api.models.loot import Loot

logger = logging.getLogger('RPG_API.inventory_controler')

def open_lootbox(body, user):  # noqa: E501
    """Open lootbox from user wich is at slot

    Open the lootbox from user wich is at slot in inventory  # noqa: E501

    :param user: the username of the user
    :type user: str
    :param slot: the slot of the lootbox
    :type slot: int

    :rtype: Inventory
    """
    loots = []
    with database.database.atomic() as ctx:
        for slot in body:
            inv = g.user.inventory[0]
            lootbox = get_object_or_404(Lootbox.select().where(inv.id == Lootbox.inventory), Lootbox.slot == slot)
            opened = inv.open_lootbox(lootbox)
            if not opened:
                ctx.rollback()
                abort(412)
            lootbox_rarety_name = lootbox.get_rarety_name()
            loot_range = CONFIG["lootbox_size_range"][lootbox_rarety_name]
            for i in range(random.randrange(*loot_range)):
                name_config = load_config('./config/name_config')
                loot_rarety = random.choices(
                    CONFIG["rarety"], 
                    CONFIG["lookup_table_lootbox_loot_distribution"][lootbox_rarety_name],
                    k=1)
                loot_complexity = random.randrange(*CONFIG["complexity_range"][loot_rarety[0]])
                loot_type = random.choice(list(CONFIG["loot_type"].keys()))
                loot_generator = CONFIG['loot_generator'][loot_type]()
                seed = hashlib.md5(str(datetime.now()).encode('utf-8')).hexdigest()

                loot_generator.generate(
                    seed=seed, 
                    dimension=CONFIG["image_dimension"], 
                    render_scale=CONFIG["image_render_scale"], 
                    output_directory=CONFIG["image_output_directory"], 
                    complexity=loot_complexity)
                name_config["loot"]["value"] = loot_type
                loot_name = RandomGenerator(name_config).generate()
                loot_name = ' '.join(x.capitalize() for x in loot_name)
                loot = Loot(
                    type=CONFIG['loot_type'][loot_type], 
                    name=loot_name,
                    image_url="{}.png".format(seed),
                    rarety=CONFIG['lootboxes_rarety'][loot_rarety[0]],
                    complexity_factor=loot_complexity)
                inv.add_item(loot)
                loots.append(loot)
        inv.rebuild_index()
    return [l.refresh() for l in loots]
