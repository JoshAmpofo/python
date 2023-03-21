#!/usr/bin/env python3
"""Packages"""

from random import choice

answers = ["Yes!", "No!", "Reply hazy", "Sorry what?"]


def give():
    """Return random choice"""
    return choice(answers)
