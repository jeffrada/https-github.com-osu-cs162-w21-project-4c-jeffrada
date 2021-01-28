# Author: Adam Jeffries
# Date: 1/27/2021
# Description: Modifies an insertion list to produce a string rather than numbers.

def string_sort(a_list):
    """
    A sorted list of strings in alphabetical order.
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos].lower() > value.lower():
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value
