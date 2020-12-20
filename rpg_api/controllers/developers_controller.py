import connexion
import six

from rpg_api.swagger_models.inventory_item import InventoryItem  # noqa: E501
from rpg_api import util


def search_inventory(search_string=None, skip=None, limit=None):  # noqa: E501
    """searches inventory

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up inventory
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[InventoryItem]
    """
    return 'do some magic!'
