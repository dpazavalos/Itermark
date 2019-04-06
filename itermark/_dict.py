from ._z_itermark import ItermarkEngine
from typing import Union


# todo ordered dict?
class ItermarkDict(dict, ItermarkEngine):
    """ItermarkEngine dict object, extending default dict functionality"""

    @property
    def active(self) -> any:
        """
        Get current active val, based off bookmark index. For key, see ItermarkEngine.activekey

        Returns:
                Active key, or None if len=0
        """
        # Using an iterator object, return the nth item (where n = current _mark)
        if self._is_loaded():
            for ndx, key in enumerate(self.__iter__()):    # Iterates through keys
                if ndx == self._mark:
                    return self[key]

    @active.setter
    def active(self, val: Union[any, dict]):
        """
        Set active dict value, based on currently marked key

        Args:
            val: new value for dict val
        """

        if self._is_loaded():
            for ndx, key in enumerate(self.__iter__()):
                if ndx == self._mark:
                    self[key] = val
        # self[self.active] = val


            # self[self._mark] = val

    @property
    def activekey(self):
        """Get active key, rather than value"""
        if self._is_loaded():
            for ndx, key in enumerate(self.__iter__()):    # Iterates through keys
                if ndx == self._mark:
                    return key


'''def new_itermarkdict():
    return ItermarkDict()'''


'''
from itermark import _dict
test = _dict.ItermarkDict({1: 'one', 2: 'two', 3: 'three'})

'''