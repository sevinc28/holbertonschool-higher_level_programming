#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create an empty list to store the results
    result = []
    
    # Iterate through each number in my_list
    for num in my_list:
        # Check if the number is divisible by 2
        result.append(num % 2 == 0)
    
    # Return the result list
    return result
