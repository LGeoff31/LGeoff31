class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="": return 0

        lps = [0] * len(needle)
        prevLPS, i = 0, 1
        #creating LPS
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = 1 + prevLPS
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
        
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                if j == 0: i +=1
                else: j = lps[j-1]
            
            if j == len(needle): return i - len(needle)

        return -1