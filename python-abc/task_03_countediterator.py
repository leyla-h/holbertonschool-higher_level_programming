#!/usr/bin/python3
"""
This module defines the CountedIterator class.
It wraps an iterator and keeps track of the number of items fetched.
"""


class CountedIterator:
    """
    Iterator wrapper that counts the number of items iterated over.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator and the counter.

        Args:
            iterable: Any object that can be converted into an iterator.
        """
        self.__iterator = iter(iterable)
        self.__counter = 0

    def get_count(self):
        """
        Returns the current number of items that have been iterated.
        """
        return self.__counter

    def __next__(self):
        """
        Fetches the next item and increments the counter.

        Raises:
            StopIteration: When there are no more items to iterate.
        """
        try:
            item = next(self.__iterator)
            self.__counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Returns the iterator object itself.
        Required to make the class an iterator.
        """
        return self
