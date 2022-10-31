#!/usr/bin/python3
"""
Module to replace element in list without modifying original list
"""

def new_in_list(my_list, idx, new_element):
    new_list = my_list[:]
    new_list[idx] = new_element
    return new_list