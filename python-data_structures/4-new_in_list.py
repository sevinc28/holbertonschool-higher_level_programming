#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the list to ensure the original list is not modified
    new_list = my_list[:]
    
    # Check if the index is valid
    if idx >= 0 and idx < len(my_list):
        new_list[idx] = element  # Replace the element at the given index
    
    return new_list  # Return the new list
