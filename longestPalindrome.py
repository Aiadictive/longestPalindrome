class Solution(object):
    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """
        if (s == None or len(s) < 1):
            return ""
        start,end = 0,0
        i=0
        while i<len(s):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            if (length > end-start):
                start = i - (length - 1) // 2
                end = i + length  // 2 
            i=i+1
        return s[start:end+1]
    
    
    
    
def expandAroundCenter(s,left,right):
    L,R = left,right  
    while (L >= 0 and R < len(s) and s[L] == s[R]):
        L=L-1
        R=R+1
    return R-L-1
        