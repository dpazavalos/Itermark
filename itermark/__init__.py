"""
Extensions of iterable data types, enabling bounds wise bookmarking indexing and active item setting
Enables iterable passing while preserving bookmarks
"""

def handler:
    if isinstance(iterable, set):
        pass
        # todo extended type acceptance
        # tuple().__init__()
    elif isinstance(iterable, list):
        super().__init__(iterable)
    elif isinstance(iterable, str):
        super().__init__([iterable])
    elif not iterable:
        super().__init__([])
    else:
        raise TypeError("Currently unsupported type")

