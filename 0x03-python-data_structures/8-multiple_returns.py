#!/usr/bin/python3


def multiple_returns(sentence):
    """Function that returns a tuple with the length of a string
    and its first character
    """
    if not sentence:
        return (len(sentence), None)
    return (len(sentence), sentence[0])
