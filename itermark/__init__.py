"""
Extensions of iterable data types, enabling bounds wise bookmarking indexing and active item setting
Enables iterable passing while preserving bookmarks
"""


class _Itermark:
    def __init__(self, iterable):
        ...

    def __new__(self, iterable):
        if isinstance(iterable, dict):
            from ._dict import ItermarkDict
            return ItermarkDict(iterable)

        elif isinstance(iterable, list):
            from ._list import ItermarkList
            return ItermarkList(iterable)

        elif isinstance(iterable, set):
            from ._set import ItermarkSet
            return ItermarkSet(iterable)

        elif isinstance(iterable, str):
            from ._str import ItermarkStr
            return ItermarkStr(iterable)

        elif isinstance(iterable, tuple):
            from ._tuple import ItermarkTuple
            return ItermarkTuple

        else:
            raise TypeError(f"Currently unsupported type! \n {type(iterable)}")


def Itermark(iterable):
    # todo this will be what user interacts with. Name appropriately

    if isinstance(iterable, dict):
        from ._dict import ItermarkDict
        return ItermarkDict(iterable)

    elif isinstance(iterable, list):
        from ._list import ItermarkList
        return ItermarkList(iterable)

    elif isinstance(iterable, set):
        from ._set import ItermarkSet
        return ItermarkSet(iterable)

    elif isinstance(iterable, str):
        from ._str import ItermarkStr
        return ItermarkStr(iterable)

    elif isinstance(iterable, tuple):
        from ._tuple import ItermarkTuple
        return ItermarkTuple

    else:
        raise TypeError(f"Currently unsupported type! \n {type(iterable)}")
