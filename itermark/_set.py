from ._z_itermark import Itermark


class ItermarkSet(set, Itermark):
    """Itermark set object, extending default set functionality"""


def new_itermarkset():
    return ItermarkSet()
