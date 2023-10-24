
def longestConsecutive(self, nums: List[int]) -> int:
    # hashmap will store the starting number from where the sequence starts and the length of the sequence
    sequence_starters = {}
    # This will eliminate any duplicates
    sequence_set = set(nums)

    # if the (current number - 1) does not exist in the set, that means it is the starter of a sequence
    # then while you are at the starter, increment it by 1 every time to check if it exists in the set
    # if it does then increment the length
    for curr in sequence_set:
        if curr-1 not in sequence_set:
            sequence_starters[curr] = 1
            temp = curr+1
            while temp in sequence_set: 
                sequence_starters[curr] += 1
                temp += 1
        else: continue
    
    # at this point, you will all the lengths of the sequences and then return the max from the hashset
    # default = 0 for empty input array
    return max(sequence_starters.values(), default=0)