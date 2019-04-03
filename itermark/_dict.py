from . import Itermark


class ItermarkDict(dict, Itermark):
    """Itermark list object, extending default list functionality"""

    @property
    def active(self) -> any:
        """
        Get current active item, based off bookmark index

        Returns:
                Active item, or None if len=0
        """
        if self._is_loaded():
            return self[self._mark]
        return None

    @active.setter
    def active(self, val: any):
        """
        Set active list item, based on current mark value

        Args:
            val: new value for current actively marked list item
        """
        if self._is_loaded():
            self[self._mark] = val



def new_itermarkdict():
    return ItermarkDict()


