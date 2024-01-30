from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        longest_plaindrome_length = 0
        odd_count_found = False
        s_counter = Counter(s)

        for count in s_counter.values():
            if count % 2 == 0:
                longest_plaindrome_length += count
            else:
                odd_count_found = True
                longest_plaindrome_length += count - 1  
            
        # Add one more if there's a character with an odd count
        if odd_count_found:
            longest_plaindrome_length += 1
        
        return longest_plaindrome_length
        
