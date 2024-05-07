class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buf = {}
        for i,v in enumerate(nums):
            print(i,v)
            buf[v] = i
            print(buf)
            if len(buf.keys()) > 1:
                if (target-v) in buf:
                    return [buf[target-v],i]


ts = Solution()
print(ts.twoSum([2,7,11,15],9))                    