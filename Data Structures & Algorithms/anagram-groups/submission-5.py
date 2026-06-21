class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen={}

        for i in strs:
            temp = i
            i = "".join(sorted(i))

            if i in seen:
                seen[i].append(temp)
            else:
                seen[i] = [temp]
        return list(seen.values())
                

        