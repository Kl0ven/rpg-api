import connexion
import six
from flask import g
from rpg_api import util
import logging
logger = logging.getLogger('RPG_API.balance_controler')

def get_balance(user):  # noqa: E501
    """Get balance information for a specific user

    Return the balance of a specific user   # noqa: E501

    :param user: the username of the user
    :type user: str

    :rtype: Balance
    """
    return {"balance": g.user.balance}
