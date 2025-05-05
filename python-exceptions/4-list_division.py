#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Check if the indices are within the range of both lists
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            # Ensure that both elements are either integers or floats
            if not isinstance(my_list_1[i], (int, float)) or not
