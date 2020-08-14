"""
Base engine for itermark functionality.

Extension for iterable data types; adds boundwise bookmark iteration, enabling
active item tracking/setting (type allowing)
"""

from typing import Optional
from ._z_itermark_exceptions import ItermarkError


class ItermarkIndicator:
    """Indication that item is itermark. Equipped on index 0"""


class _ItermarkEngine:
    """
    Itermark functions, to build on top of default iterable object types
    Type specifics inherit and supplement with any needed functions/properties

    - mark: Bookmark index of underlying iterable. Supports direct and
    operator assignment
    - active: Active item based off mark index. Read/write usage, type allowing
    """

    # Note: Because all public functions use _ensure_loaded(), any internal
    #  calls to these functions will cause recursion. Code should only call
    #  private functions

    _mark: int = None
    """Protected bookmark index; access via mark() so boundary checks are 
    run. When there are no entries, _mark is set to None"""

    def __iter__(self):
        return iter(self[1:-1])

    def __str__(self):
        return str(self[1:-1])

    def __next__(self):
        """Emulates default list_iterator next. When reaches end of list,
        throws StopIteration. Mark remains at [-1]"""
        try:
            self._ensure_loaded()
            active_to_return = self.active
            self._mark += 1
        except IndexError:
            raise StopIteration('End of itermark iteration. set mark to -1 '
                                 'or reset to 0') from None
        return active_to_return

    @property
    def mark(self) -> Optional[int]:
        """
        Get current active bookmark index

        Returns:
                Active bookmark index, or None if len=0
        """
        # Note: Because all user-accessable functions use ._is_loaded,
        # any code calls to public functions
        self._ensure_loaded()
        return self._mark

    @mark.setter
    def mark(self, new_mark: int):
        """
        Attempts to set active mark. Raises IndexError if new_mark is out of bounds

        Arguments:
            new_mark:
                Desired new bookmark index
        """

        mark_to_set = self._calc_if_negative_index(new_mark)
        # Preserve orig new_mark. in case of OOB, raise IndexErr w/ given mark

        # If negative index, calculate
        if mark_to_set == 0:
            raise ItermarkError('ItermarkIndicator at 0, cannot set '
                                '.mark to 0!')
        if mark_to_set not in self._mark_range:
            print(mark_to_set)
            raise IndexError(f"Given mark [{new_mark}] outside index range "
                             f"1-{self._mark_range[-1]}")

        self._mark = mark_to_set
        self._ensure_loaded()


    @property
    def active(self) -> any:
        """
        Get current active item, based off bookmark index

        Returns:
                Active item, or None if len=0
        """
        self._ensure_loaded()
        return self[self._mark]

    @active.setter
    def active(self, val: any):
        """
        Set active list item, based on current mark value

        Args:
            val: new value for current active item
        """
        self._ensure_loaded()
        self[self._mark] = val

    # _ItermarkEngine maintenance

    def _ensure_loaded(self):
        """Ensures items exist for itermark to track. If none,
        throws excpetion ItermarkNonActive.  All public functions call this
         first; calling itermark funcs on non-existent self throws errors"""
        if self._is_loaded:
            self._activate_mark()
        else:
            self._deactivate_mark()
            raise ItermarkError("No items for itermark to track!")

    def _ensure_placeholder_exists(self):
        """Due to quirk in assignment operators, """
        if not isinstance(self[0], ItermarkIndicator):
            # self.insert(0, _ItermarkPlaceHolder())
            self.insert(0, ItermarkIndicator)

    def _ensure_placeholder_not_active(self):
        """"""


    @property
    def _is_loaded(self) -> bool:
        """bool representing if items exist in self, using __len__ check.
        Seperate from _ensure_loaded so maint funcs can run a check without
        de/activating or causing recursive loop"""
        if self.__len__() == 0:
            return False
        return True

    @property
    def _mark_range(self) -> range:
        """Current acceptable bookmark range, using builtin obj's range and
        __len__"""
        return range(1, self.__len__())

    def _deactivate_mark(self):
        """Used to disable callable attributes, if iterable becomes empty"""
        self._mark = None

    def _calc_if_negative_index(self, mark_to_calc: int) -> int:
        if mark_to_calc < 0:
            if self._mark == 0:
                print('well then...')
            return self.__len__() + mark_to_calc
        return mark_to_calc

    def _activate_mark(self):
        """Current iterator has items, activate itermark"""

        if not self._mark:
            self._mark = 1
        elif self._mark not in self._mark_range:
            raise IndexError(f"Mark [{self._mark}] out of bounds [0-"
                             f"{self._mark_range[-1]}]")
