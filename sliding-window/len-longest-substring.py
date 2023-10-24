def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0: return 0

    hashmap = {}
    longest = 0
    start = 0
    for i in range(len(s)):
        if s[i] in hashmap and start <= hashmap[s[i]]:
            start = hashmap[s[i]] + 1
        else: longest = max(longest, i-start+1)
        hashmap[s[i]] = i
    
    return longest