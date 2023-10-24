def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hashmap = {}
    for s in strs:
        s_sorted = str(sorted(s))
        if s_sorted not in hashmap:
            hashmap[s_sorted] = [s]
        else: hashmap[s_sorted].append(s)
    
    output = []
    for v in hashmap.values():
        output.append(v)
    
    return output