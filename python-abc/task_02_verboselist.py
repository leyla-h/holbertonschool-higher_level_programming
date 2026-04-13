#!/usr/bin/python3
"""
Module that defines the VerboseList class.
Extends the built-in list to provide notifications on modifications.
"""


class VerboseList(list):
    """
    A class that inherits from list and prints messages
    when items are added or removed.
    """

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list and prints the number of items added."""
        items_added = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(items_added))

    def remove(self, item):
        """Prints a notification before removing an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints a notification before popping an item."""
        # Need to identify the item before it is removed
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
