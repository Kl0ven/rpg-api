import connexion
import six

from rpg_api.swagger_models.inventory_item import InventoryItem  # noqa: E501
from rpg_api.models.db import User
from rpg_api import util


def add_inventory(body=None):  # noqa: E501
    """adds an inventory item

    Adds an item to the system # noqa: E501

    :param body: Inventory item to add
    :type body: dict | bytes

    :rtype: None
    """
    u = User.create(title="huey", content='Hello!', members_only=True, )
    if connexion.request.is_json:
        body = InventoryItem.from_dict(connexion.request.get_json())  # noqa: E501
    return u.title
