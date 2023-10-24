def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {} # Stores the number of occurrences for a number (number:occurrences)
    # Stores the numbers having the same occurrences
    freq = [[] for i in range(len(nums)+1)] 

    # Count the occurrences
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # Store the numbers having the same occurences in one list
    # Eg. if 3 occurences = idx 3 will have [n1, n2, ... ]
    # Here, the last index will contain the a list of numbers having the most occurences
    for n, c in count.items():
        freq[c].append(n)

    out = []
    # Then iterate through the freq list backwards
    # Most occurences number list first.. append every number in the output and check
    # if the output list has k amount of numbers then return
    for i in range(len(freq)-1, 0, -1):
        for number in freq[i]:
            out.append(number)
            if len(out)==k: return out