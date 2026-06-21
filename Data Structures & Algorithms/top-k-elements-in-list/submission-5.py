class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen={}
        nums.sort()
        res=[]

        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1
        for _ in range(k):
            max_fre = 0
            max_num = 0

            for num,fre in seen.items():
                if fre > max_fre:
                    max_fre = fre
                    max_num = num
            res.append(max_num)
            del seen[max_num]
        
        return res
        