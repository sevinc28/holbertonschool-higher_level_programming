#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Create a new list excluding the element at idx
    return my_list[:idx] + my_list[idx+1:]
