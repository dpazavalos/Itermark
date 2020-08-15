from collections import OrderedDict
from ._dict import ItermarkDict
# from . import ItermarkIndicator


class ItermarkOrDict(ItermarkDict, OrderedDict):
    """Itermark Ordered Dict object, extending default dict functionality"""
    # Inherits ItermarkDict properties

    """def __setitem__(self, key, value):
        if key == 0:
            if value != ItermarkIndicator:
                raise ItermarkError(
                    "Cannot change or remove Itermark Indicator!")
        super().__setitem__(key, value)

    def _ensure_placeholder_exists(self): 
        try:
            if self[0] is not ItermarkIndicator:
                raise ItermarkError('iterable cannot contain key [0]!')
        except KeyError:
            new_dict = {0: ItermarkIndicator}
            new_dict.update(self)
            self.clear()
            self.update(new_dict)"""