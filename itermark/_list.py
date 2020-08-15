from ._z_itermark_engine import _ItermarkEngine
from ._z_itermark_exceptions import ItermarkError


class ItermarkList(_ItermarkEngine, list, ):
    """_ItermarkEngine string object, Adding bookmarking functionality"""
    # Works out of the box
