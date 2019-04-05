from ._z_itermark import Itermark
from typing import Union


class ItermarkDict(dict, Itermark):
    """Itermark dict object, extending default dict functionality"""

    @property
    def active(self) -> any:
        """
        Get current active key and value, based off bookmark index. Returns as single dict. For key
        /val specific, see activekey, activeval

        Returns:
                Active item, or None if len=0
        """
        # Using an iterator object, return the nth item (where n = current _mark)
        if self._is_loaded():
            for ndx, item in enumerate(self.__iter__()):    # Iterates through keys
                if ndx == self._mark:
                    return {item: self[item]}
        return None

    @active.setter
    def active(self, val: Union[any):
        """
        Set active dict key, based on current mark value

        Args:
            val: new value for current actively marked dict key
        """
        if self._is_loaded():
            self[self._mark] = val


def new_itermarkdict():
    return ItermarkDict()


test = {1: 'one', 2: 'two'}