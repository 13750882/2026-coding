# week04-4c.py (重寫 week04-4b.py)
# LeetCode 3866. First Unique Even Element
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        from collections import Counter
        H = Counter(nums)  # 使用進階資料結構, 可以統計數量
        for nn in nums:
            if nn % 2 == 0 and H[nn] == 1:  # 偶數 and 落單
                return nn
        return -1
