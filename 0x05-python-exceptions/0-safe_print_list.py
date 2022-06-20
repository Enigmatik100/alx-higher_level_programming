#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Function that prints x elements of a list using try/ catch
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()
        return count
    except IndexError:
        return count
