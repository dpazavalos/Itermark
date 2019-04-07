from ._z_itermark import ItermarkEngine


# Note that this is designed around 3.6+ dict's insertion ordered dictionaries
# Recommend a Collections.OrderedDict for earlier implementations
class ItermarkDict(dict, ItermarkEngine):
    """ItermarkEngine dict object, extending default dict functionality"""

    # Simp obj used when setting active key
    key_marker = None

    @property
    def active(self) -> any:
        """
        Get current active val, based off bookmark index. For key, see ItermarkEngine.activekey

        Returns:
                Active key, or None if len=0
        """
        # Using an iterator object, return the nth item (where n = current _mark)
        if self._is_loaded:
            for ndx, key in enumerate(self.__iter__()):    # Iterates through keys
                if ndx == self._mark:
                    return self[key]

    @active.setter
    def active(self, val: any):
        """
        Set active dict value, based on currently marked key

        Args:
            val: new value for dict val
        """

        if self._is_loaded:
            for ndx, key in enumerate(self.__iter__()):
                if ndx == self._mark:
                    self[key] = val
        # self[self.active] = val


            # self[self._mark] = val

    @property
    def activekey(self):
        """Get active key, rather than value"""
        if self._is_loaded:
            for ndx, key in enumerate(self.__iter__()):    # Iterates through keys
                if ndx == self._mark:
                    return key

    @activekey.setter
    def activekey(self, new_key: any):
        """
        Set active key

        Note: Dict keys are immutable! Itermark gets around this by creating a new
        dict, which in complexity terms is a Big O No
        """
        # raise AttributeError("You shouldn't be trying to change a dict's key!")

        # Bubble inspired replace
        if self._is_loaded:

            dict_after_mark = []    # (key, val)
            # list used to preserve order
            keys_to_pop = set()
            # A second set costs little in mem while offering faster iteration when popping
            # ( On a dict with 4 mil entires, popping with a set cut time from 4.5s to 3.7 s)
            # (And recall that we can't pop dict entries WHILE iterating)

            if not self.key_marker:
                self.key_marker = KeyMarker()
            else:
                self.key_marker.reset()

            for ndx, key in enumerate(self.__iter__()):

                # Once key_marker is found, begin adding orig key/val to dict_after_mark set
                if self.key_marker.found:
                    dict_after_mark.append((key, self[key]))
                    keys_to_pop.add(key)

                # Find active key, add it's val bound to our new key
                if ndx == self._mark:
                    self.key_marker.new(key)
                    dict_after_mark.append((new_key, self[key]))
                    keys_to_pop.add(key)

            # <1s/1 mil dict entries after active key/val
            # recall that our first key is the new version of the mark key.
            # Pop old active key, it's being replaced with our new one
            self.pop(self.key_marker.mark_key)
            for k in keys_to_pop:
                try:
                    self.pop(k)
                except KeyError:
                    pass

            # Add all our old dict entries
            for ndx, k_v in enumerate(dict_after_mark):
                k, v = k_v
                self[k] = v


class KeyMarker:
    """Simp obj used when setting active key"""
    found = False
    mark_key: any

    # no recasting multiple init functions. Reuse one single obj
    def new(self, mark_key):
        """
        Args:
            mark_key: the current Active key (typically found through separate iteration, rather
            than calling ItermarkDict.activekey
        """
        self.found = True
        self.mark_key = mark_key

    def reset(self):
        """
        Reset to default, mark_key not found settings
        """
        self.found = False
        self.mark_key = None
