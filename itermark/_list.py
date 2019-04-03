from . import Itermark


class ItermarkList(list, Itermark):
    """Itermark list object, extending default list functionality"""


def new_itermarklist():
    return ItermarkList()
