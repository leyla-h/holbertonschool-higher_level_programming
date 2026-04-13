#!/usr/bin/python3
"""
This module defines mixin classes for swimming and flying,
and a Dragon class that combines both functionalities.
"""


class SwimMixin:
    """Mixin to add swimming capability to a creature."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying capability to a creature."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits capabilities from SwimMixin and FlyMixin.
    """

    def roar(self):
        """Prints a roaring message specific to dragons."""
        print("The dragon roars!")
