from ._z_itermark_engine import _ItermarkEngine
from ._z_itermark_exceptions import ItermarkError

class ItermarkList(_ItermarkEngine, list, ):
    """_ItermarkEngine string object, Adding bookmarking functionality"""
    # Works out of the box

    def __setitem__(self, key, value):
        if key == 0:
            raise ItermarkError("Cannot change or remove Itermark Indicator!")
        super().__setitem__(key, value)



t = ItermarkList([1, 2, 3])
