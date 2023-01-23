def insertion_sort(list):
    # Since the 0th index in the list will be sorted by default (single number is sorted inherently), 
    # you start from the 1st index of the list
    for index in range(1, len(list)):
        value = list[index]
        j = index - 1

        # Now, you compare each value to the previous one and check if it is less than it, 
        # If it is then you shift the values to place the lower value in it's spot
        while(j >= 0 and value < list[j]):
            list[j+1] = list[j]
            j -= 1
        
        # If the value is not lower, then you found where the value should be placed. Place it on that index
        list[j+1] = value
    
    return list


# Result = [1,2,3,5,6,8]
example = [3, 6, 5, 8, 2, 1]
print(insertion_sort(example))