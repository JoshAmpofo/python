#!/usr/bin/env python3
"""Working with modules"""

from random import choice

places = ["Papa Ye", "Papa's Pizza", "Baritos",
          "Chicken Inn", "Peter Pan"]


def pick():
    """Return a fast food place"""
    return choice(places)
