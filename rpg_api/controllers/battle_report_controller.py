import connexion
import six
from flask import g, send_from_directory
from rpg_api import util
import logging, datetime
from rpg_api.models import database
from rpg_api.models.battle_report import Battle_report
from rpg_api.models.lootbox import Lootbox
from playhouse.flask_utils import get_object_or_404
from config import CONFIG
import json
logger = logging.getLogger('RPG_API.balance_controler')


def get_battle_reports(user):  # noqa: E501
    """Get battle report information for a specific user

    Return a list of all visible battle report of a specific user   # noqa: E501

    :param user: the username of the user
    :type user: str

    :rtype: list of minimal battle report
    """
    brs = []
    now = datetime.datetime.now()
    for br in g.user.battle_reports:
        if br.end_date < now: 
            brs.append({"id": br.br_id, "date": br.start_date, "new": not br.opened})
    return brs


def get_battle_report(user, id_):
    with database.database.atomic() as ctx:
        br = get_object_or_404(Battle_report.select().where(g.user.id == Battle_report.user), Battle_report.br_id == id_)
        if not br.opened:
            br.opened = True
            g.user.balance += br.money
            lootboxes_data = json.loads(br.lootboxes_data)
            inv = g.user.inventory[0]
            lootboxes = []
            for _ in range(lootboxes_data['nb']):
                lb = Lootbox(rarety=lootboxes_data["lb_rarety"])
                inv.add_item(lb)
                lootboxes.append(lb)
            br.save()
            g.user.save()
            br.first_opening = True
            br.lootboxes = lootboxes
    return br


def get_full_report(user, id_):
    return send_from_directory(CONFIG["reports_output_directory"], "{}.txt".format(id_))
