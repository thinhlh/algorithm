# Solved 

# First we will find the occurence of each char, if a char's occurence is even => Then all char will combine to a palidrome
# If we have k char have odd number of occurence, they will be combined, however, only k-1 characters will combine to palidrome
# Etc: aaa-bbb-ccc-dd | k=3 meaning 3 characters has odd numbers => we have to exclude k-1 number of characters => 2, etc  => 
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        occurences = {}
        
        for i in s:
            if i in occurences:
                occurences[i]+=1
            else:
                occurences[i] = 1
            
        max_even = 0
        max_odd = 0     
        for value in occurences.values():
            if value%2==0:
                max_even+=value
            else:
                max_odd +=1
        return len(s) if max_odd<=1 else len(s)-(max_odd-1)

# print(Solution().longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'))
print(Solution().longestPalindrome('aaabbbcccdd'))