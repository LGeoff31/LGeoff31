class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        n, new_nums = len(nums), []

        for i in range(1,n):
            if nums[i] > nums[i-1]:
                new_nums.append(1)
            elif nums[i] == nums[i-1]:
                new_nums.append(0)
            else:
                new_nums.append(-1)

        def lps(pattern):
            m = len(pattern)

            dp = [0]*m 

            i,j = 1,0 

            while i < m:
                if pattern[i] == pattern[j]:
                    dp[i] = j+1 
                    i += 1 
                    j += 1 
                else:
                    if j == 0:
                        i += 1
                    else:
                        j = dp[j-1]

            return dp 


        def KMPSearch(new_nums,pattern):
            n,m = len(new_nums),len(pattern)

            i,j = 0,0 

            total,ans = 0,lps(pattern)

            while (n-i) >= (m-j):
                if pattern[j] == new_nums[i]:
                    i += 1 
                    j += 1 

                if j == m:
                    total += 1 
                    j = ans[j-1]
                elif i < n and pattern[j] != new_nums[i]:
                    if j:
                        j = ans[j-1]
                    else:
                        i += 1 

            return total 

        return KMPSearch(new_nums,pattern)



        