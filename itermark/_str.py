from ._z_itermark_engine import _ItermarkEngine


class ItermarkStr(str, _ItermarkEngine):
    """_ItermarkEngine string object, Adding bookmarking functionality"""
    # Works out of the box
