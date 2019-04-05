"""
Base engine for itermark functionality.

Extensions of iterable data types, enabling bounds wise bookmarking indexing and active item setting
Enables iterable passing while preserving bookmarks
"""

from typing import Optional


class Itermark:
    """
    Extension of default iterator objects. Stores and preserves a boundwise bookmark

    Extension of default iterable obj. Stores and preserves a bound wise bookmarking index that will
    never go outside of the underlying iterable's boundaries.
    Whole iterable can be passed between objects with bookmark

    - mark: Bookmark index of underlying iterable. Supports direct and operator assignment
    - active: Active item, based off current mark index. Allows read/write usage
    """

    _mark = None
    """Protected bookmark index; access via property mark"""

    @property
    def mark(self) -> Optional[int]:
        """
        Get current active bookmark index

        Returns:
                Active bookmark index, or None if len=0
        """
        if self._is_loaded():
            return self._mark
        return None

    @mark.setter
    def mark(self, new_mark: int):
        """
        Attempts to set active mark, within bounds. OoBs marks are overwritten with closest bound

        Arguments:
            new_mark:
                Desired new bookmark index
        """
        if self._is_loaded():
            if not isinstance(new_mark, int):
                raise TypeError(f"marklist index must be integer, not {str(type(new_mark))}")

            # No negatives. -= 1 fouls up indexing when _mark is 0
            if new_mark < 0:
                self._mark = 0

            # Max length check
            elif self._mark >= self.__len__():
                self._mark = self.__len__() - 1

            else:
                self._mark = new_mark

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
            val: new value for current active item
        """
        if self._is_loaded():
            self[self._mark] = val

    # Itermark maintenance

    def _is_loaded(self) -> bool:
        """Used to prevent itermark functions if iterable is empty. itermark functions call this"""
        if self.__len__() == 0:
            self._deactivate_mark()
            return False
        self._activate_mark()
        return True

    def _deactivate_mark(self):
        """Used to disable callable attributes, if iterable becomes empty"""
        self._mark = None

    def _activate_mark(self):
        """Ensures _ndx is activated and within bounds. Iterable is assumed non-empty"""
        if not self._mark or self._mark < 0:
            self._mark = 0
        if self._mark >= self.__len__():
            self._mark = self.__len__() - 1

    def _get_mark_via_iter_obj(self):

        pass



    # Hollow references, to be overwritten by each subtypes' specific version.
    # Itermark functions will then reference the actual function

    def __len__(self):
        """Hollow reference. Itermark types use default types first, so this will not overwrite"""
        pass

    def __iter__(self):
        """Hollow reference. Itermark types use default types first, so this will not overwrite"""
        return [1, 2, 3]

    def __getitem__(self):
        """Hollow reference. Itermark types use default types first, so this will not overwrite"""
        pass

    def __setitem__(self):
        """Hollow reference. Itermark types use default types first, so this will not overwrite"""
        pass
