from ._z_itermark import Itermark


class ItermarkList(list, Itermark):
    """Itermark list object, extending default list functionality"""

    def __init__(self, iterable):
        super(list).__init__(iterable)



def new_itermarklist():
    return ItermarkList()
