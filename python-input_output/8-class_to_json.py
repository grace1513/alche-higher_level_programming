#!/usr/bin/python3
"""Module that returns dictionary description of an object for JSON."""


def class_to_json(obj):
    """Return dictionary description of a class for JSON serialization."""
    return obj.__dict__
