class Solution(object):
    def maximumLengthSubstring(self, s):
        count = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1

            while count[char] > 2:
                left_char = s[left]
                count[left_char] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length