def lastStoneWeight(self, stones: List[int]) -> int:
    stones = [-x for x in stones]
    heapq.heapify(stones)

    while(len(stones) > 1):
        x = -heapq.heappop(stones)
        y = -heapq.heappop(stones)
        if x == y: continue
        elif x != y:
            heapq.heappush(stones, -(abs(y-x)))

    return abs(stones[0]) if len(stones) == 1 else 0