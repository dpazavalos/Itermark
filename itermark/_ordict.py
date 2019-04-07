from collections import OrderedDict
from ._dict import ItermarkDict


# Note that this is designed around 3.6+ dict's insertion ordered dictionaries
# Recommend a Collections.OrderedDict for earlier implementations
class ItermarkOrDict(OrderedDict, ItermarkDict):
    """Itermark Ordered Dict object, extending default dict functionality"""
    # Inherits active properties from ItermarkDict
