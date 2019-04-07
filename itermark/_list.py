from ._z_itermark import ItermarkEngine


class ItermarkList(list, ItermarkEngine):
    """ItermarkEngine string object, Adding bookmarking functionality"""
    # Works out of the box
