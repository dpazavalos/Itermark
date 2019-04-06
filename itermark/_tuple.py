from ._z_itermark import ItermarkEngine


class ItermarkTuple(tuple, ItermarkEngine):
    """ItermarkEngine Tuple object, Adding bookmarking functionality"""
