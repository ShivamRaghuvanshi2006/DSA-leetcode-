class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sa=sum(aliceSizes); sb=sum(bobSizes); delta=(sa-sb)//2
        s=set(bobSizes)
        for a in aliceSizes:
            if a-delta in s: return [a,a-delta]
        return []