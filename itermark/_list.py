from ._z_itermark import ItermarkEngine


class ItermarkList(list, ItermarkEngine):
    """ItermarkEngine string object, Adding bookmarking functionality"""


    # def __init__(self, iterable):
    #     super(list).__init__(iterable)


'''class NewItermarkList:
    def __init__(self, iterable):
        ...

    def __new__(cls, iterable):
        return ItermarkList(iterable)'''


def new_itermarklist(iterable):
    return ItermarkList(iterable)
