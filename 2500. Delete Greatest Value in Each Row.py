"""
遞迴
"""
# class Solution:
#     def deleteGreatestValue(self, grid) -> int:
#         return self.process(grid,0)

#     def process(self,grid,total):
#         import numpy

#         new_list=[]
#         find_max=[]
#         #print(grid)
#         for x in grid:  
#             find_max.append(numpy.max(x))
#             x.remove(numpy.max(x))
#             new_list.append(x)
#         total+=numpy.max(find_max)
#         if not x:
#             return total
#         return self.process(new_list,total)

"""
先排序大小，之後重新包裝
每個row一樣大小會在一起 [1,2,3][4,5,6]->[1,4][2,5][3,6]
把一樣大小的大值相加就好了

"""
class Solution:
    def deleteGreatestValue(self, grid) -> int:
        grid = [list(sorted(row)) for row in grid]
        return sum(map(max, zip(*grid)))

if __name__ == '__main__':
    ans=Solution()
    print(ans.deleteGreatestValue([[1,2,4],[3,3,1]]))