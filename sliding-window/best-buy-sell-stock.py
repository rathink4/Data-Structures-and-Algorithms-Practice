def maxProfit(self, prices: List[int]) -> int:
    maxval = 0
    minPrice = 1000000
    for e in prices:
        minPrice = min(minPrice, e)
        maxval = max(maxval, e - minPrice)
    return maxval