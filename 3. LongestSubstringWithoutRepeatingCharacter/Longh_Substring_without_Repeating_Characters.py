

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charIndexMap= {}

        start = 0
        max_lenght = 0

        for end in range (len(s)):
            if s[end] in charIndexMap and charIndexMap[s[end]] >=start:
                start = charIndexMap[s[end]] + 1

            charIndexMap[s[end]] = end

            max_lenght = max(max_lenght,end - start + 1)

        return max_lenght
    


if __name__ == "__main__":
    solution = Solution()
    
    # Test 1
    s1 = "abcabcbb"
    print("Test 1 - Expected: 3")
    print("Output:", solution.lengthOfLongestSubstring(s1))
    
    # Test 2
    s2 = "bbbbb"
    print("\nTest 2 - Expected: 1")
    print("Output:", solution.lengthOfLongestSubstring(s2))
    
    # Test 3
    s3 = "pwwkew"
    print("\nTest 3 - Expected: 3")
    print("Output:", solution.lengthOfLongestSubstring(s3))