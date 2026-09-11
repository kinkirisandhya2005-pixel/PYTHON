class Solution(object):
    def totalNumbers(self, digits):
        from itertools import permutations
        
        numbers = set()
        
        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                numbers.add(a * 100 + b * 10 + c)
        
        return len(numbers)