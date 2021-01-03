import connexion
import six
from flask import g
from rpg_api import util
import logging
logger = logging.getLogger('RPG_API.hero_controler')


def get_hero(user):  # noqa: E501
    """Get hero information for a specific user

    Return the hero  of a specific user   # noqa: E501

    :param user: the username of the user
    :type user: str

    :rtype: Hero
    """

    return g.user
