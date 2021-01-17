import connexion
import six
from flask import g, abort, make_response
from rpg_api import util
import logging
from config import CONFIG
from rpg_api.models import database, User, Battle_report
from rpg_api.dungeon.reporter import Reporter
from rpg_api.dungeon.dungeon import Dungeon
from playhouse.flask_utils import get_object_or_404
from datetime import datetime, timedelta
import random
import json
logger = logging.getLogger('RPG_API.crawl_dungeon')


def crawl_dungeon(body, user):  # noqa: E501
    """Select Loot from user wich is at slot

    select the Loot(s) from user wich is at slot in inventory  # noqa: E501

    :param body: the slot(s) of the loot(s)
    :type body: List[]
    :param user: the username of the user
    :type user: str

    :rtype: None
    """
    users = [g.user]
    for username in body:
        users.append(get_object_or_404(User.select(), User.name == username))

    
    for user in users:
        if user.status != CONFIG["status"]["Idle"]:
            abort(412, "{} already crawling dungeon".format(user.name))

    with database.database.atomic() as ctx, Reporter() as reporter:
        d = Dungeon(users, reporter)
        resultat = d.crawl()
        report = reporter.save()
        for user in users:
            rooms, fleeing, health = resultat[user.name.capitalize()]
            elapsed_time = timedelta(minutes=rooms*CONFIG["minutes_per_room"])
            end_time = datetime.now() + elapsed_time
            money = get_money_from_room(rooms)
            lb_rarety, nb = get_lb_stats(rooms)

            # set state to crawling and end_date of state
            # set user health
            user.start_crawling(end_time)
            health = 0 if health < 0 else health
            # create battle report
            b = Battle_report.create(
                    user=user, 
                    end_date=end_time,
                    full_report=report,
                    is_fleeing=fleeing,
                    health=health,
                    money=money,
                    lootboxes_data=json.dumps({"lb_rarety": lb_rarety, "nb": nb})
                )
            b.save()
            user.save()
    return "", 200

def get_money_from_room(r):
    return ((r * (r + 1)) / 2) * CONFIG["money_coef"]


def get_lb_stats(r):
    for i in CONFIG['lootboxes_rarety_by_rooms_range']:
        rmin = i['range'][0]
        rmax = i['range'][1]
        if r >= rmin and r <= rmax:
            return i['rarety'], random.randrange(*i['nb_lootboxes'])
