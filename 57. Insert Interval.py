from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        t_l,t_r=newInterval
        ans=[]
        appended=False

        if not intervals:
            return [newInterval]

        for l,r in intervals:
            if t_r<l and not appended:
                ans.append([t_l,t_r])
                appended=True

            if r<t_l or l>t_r:
                ans.append([l,r])
            else:
                if r>=t_l>=l:
                    t_l=min(t_l,l)
                if r>=t_r>=l:
                    t_r=max(t_r,r)
                    ans.append([t_l,t_r])
                    appended=True

        if not appended:
            ans.append([t_l,t_r])

        return ans

if __name__=='__main__':
    sum=Solution()
    print( sum.insert( intervals = [[1,5]], newInterval = [2,7] ))

'''
leetcode ans
邏輯相同 但程式更加精簡流暢
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            result = []

            for idx, interval in enumerate(intervals):
                17,18行指需要判斷前面
                if interval[1] < newInterval[0]:
                    result.append(interval)

                不該把前後判斷放在一起 判斷後面出現更大的就該直接回傳 
                寫在一起 沒辦法直接回傳
                所以導致要多一個變數紀錄有沒有新增過 再出現更大的值前先加進去
                遇到沒有更大的值的狀況也不能直接新增 要透過變數檢查是否新增過

                elif interval[0] > newInterval[1]:
                    result.append(newInterval)
                    return result + intervals[idx:]
                else:
                    20~25行可以縮短成53
                    # here, we update the new Interval
                    newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

            # this is one of the keys
            result.append(newInterval)
            
            return result
        
'''