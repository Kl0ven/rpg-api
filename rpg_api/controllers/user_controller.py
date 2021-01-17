import connexion
import six
from flask import g
from rpg_api import util
from rpg_api.models.user import User
import logging
logger = logging.getLogger('RPG_API.balance_controler')


def get_users():  # noqa: E501
    users = User.select().execute()
    return list(users)
