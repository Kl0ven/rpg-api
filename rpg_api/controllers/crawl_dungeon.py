import connexion
import six
from flask import g, abort, make_response
from rpg_api import util
import logging
from config import CONFIG
from rpg_api.models import database, User
from rpg_api.dungeon.reporter import Reporter
from rpg_api.dungeon.dungeon import Dungeon
from playhouse.flask_utils import get_object_or_404

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
        d.crawl()

        res = reporter.get_log()

    response = make_response(res, 200)
    response.mimetype = "text/plain"
    return response

