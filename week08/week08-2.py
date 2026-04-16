# week08-2.py 學習計畫 Binary Search 第 1 題
# 題目給妳一個 guess(num) 函式，妳可以呼叫它來找出 1...n 範圍內的「隱藏答案」

import bisect

class Solution:
    def guessNumber(self, n: int) -> int:

        ### 方法 1：神奇的 bisect_left() 寫法，只要 1 行 ###
        # 這個方法是利用 Python 內建的二元搜尋工具。
        # 邏輯：將 guess(x) 的結果取負號，讓數列呈現「由小到大」的趨勢，進而定位 0 的位置。
        # 一行就能抵擋下面 7 行的迴圈邏輯。
        # return bisect.bisect_left(range(n + 1), 0, key=lambda x: -guess(x))

        # -----------------------------------------------------------

        ### 方法 2：標準二元搜尋 (while 迴圈) ###
        # 為什麼要用這個？因為當 n 有 20 億這麼大時，暴力法 (for 迴圈) 試不完。
        # 要用小學「猜數字」遊戲邏輯：每次範圍猜一半，根據提示縮小範圍。

        left, right = 1, n + 1  # 設定左右邊界 (左「包含」、右「不包含」)

        while left < right:     # 當左右範圍還沒有「撞在一起」之前繼續執行
            mid = (left + right) // 2  # 猜中間的數

            res = guess(mid)

            if res == 0:        # 恰好猜中
                return mid

            if res > 0:         # 提示：答案更高一點
                left = mid + 1  # 將中點設為下界，往右邊找
            else:               # 提示：答案更低一點
                right = mid     # 將中點設為上界，往左邊找

        return left
