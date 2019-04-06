from ._z_itermark import ItermarkEngine


class ItermarkStr(str, ItermarkEngine):
    """ItermarkEngine string object, Adding bookmarking functionality"""
