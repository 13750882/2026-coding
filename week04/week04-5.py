# week04-5.py 學習計畫 prefix sum 第2題
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0]  # 初始化前綴和陣列
        for i in range(N):
            prefix.append(prefix[-1] + nums[i])  # 累計前綴和

        postfix = [0] * (N + 1)
        for i in range(N-1, -1, -1):
            postfix[i] = postfix[i+1] + nums[i] # 累計後綴和

        for i in range(N):
            if prefix[i] == postfix[i+1]: return i # 比對中心點左右
        return -1
