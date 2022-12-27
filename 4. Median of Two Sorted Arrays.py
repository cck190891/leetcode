class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        addlist=sorted(nums1+nums2)
        if len(addlist)%2==0:
            mid=float((addlist[int(len(addlist)/2)]+addlist[int(len(addlist)/2)-1]))/2
        else:
            mid=addlist[int(len(addlist)/2)]
        return mid    

if __name__=='__main__':
    output=Solution()
    print(output.findMedianSortedArrays([1,2],[3,4]))
    