class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        odd = [i for i in range(26) if cnt[i] % 2 == 1]

        if len(odd) > 1:
            return ""
        mid = chr(odd[0] + ord('a')) if odd else ""
        half_cnt = [c // 2 for c in cnt]
        m = n // 2

        def make_palindrome(left):
            if n % 2 == 0:
                return left + left[::-1]
            else:
                return left + mid + left[::-1]
        left_target = target[:m]

        used = [0] * 26
        possible = True

        for ch in left_target:
            x = ord(ch) - ord('a')
            used[x] += 1
            if used[x] > half_cnt[x]:
                possible = False

        if possible:
            candidate = make_palindrome(left_target)

            if candidate > target:
                return candidte
        prefix_used = [None] * (m + 1)
        prefix_used[0] = [0] * 26

        for i in range(m):
            prefix_used[i + 1] = prefix_used[i][:]

            x = ord(target[i]) - ord('a')
            prefix_used[i + 1][x] += 1

        for i in range(m - 1, -1, -1):
            used = prefix_used[i]
            ok = True
            for c in range(26):
                if used[c] > half_cnt[c]:
                    ok = False
                    break

            if not ok:
                continue

            x = ord(target[i]) - ord('a')
            for y in range(x + 1, 26):
                if used[y] < half_cnt[y]:
                    left = list(target[:i])
                    left.append(chr(y + ord('a')))

            
                    remaining = half_cnt[:]

                    for ch in left:
                        remaining[ord(ch) - ord('a')] -= 1

                    for c in range(26):
                        if remaining[c] > 0:
                            left.extend([chr(c + ord('a'))] * remaining[c])

                    left = ''.join(left)

                    return make_palindrome(left)

        return ""
class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)

        
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        
        odd = [i for i in range(26) if cnt[i] % 2 == 1]

        if len(odd) > 1:
            return ""

        
        mid = chr(odd[0] + ord('a')) if odd else ""

        
        half_cnt = [c // 2 for c in cnt]
        m = n // 2

        def make_palindrome(left):
            if n % 2 == 0:
                return left + left[::-1]
            else:
                return left + mid + left[::-1]

        
        left_target = target[:m]

        used = [0] * 26
        possible = True

        for ch in left_target:
            x = ord(ch) - ord('a')
            used[x] += 1
            if used[x] > half_cnt[x]:
                possible = False

        if possible:
            candidate = make_palindrome(left_target)

            if candidate > target:
                return candidate

        
        prefix_used = [None] * (m + 1)
        prefix_used[0] = [0] * 26

        for i in range(m):
            prefix_used[i + 1] = prefix_used[i][:]

            x = ord(target[i]) - ord('a')
            prefix_used[i + 1][x] += 1

        for i in range(m - 1, -1, -1):
            used = prefix_used[i]

        
            ok = True
            for c in range(26):
                if used[c] > half_cnt[c]:
                    ok = False
                    break

            if not ok:
                continue

            x = ord(target[i]) - ord('a')

    
            for y in range(x + 1, 26):
                if used[y] < half_cnt[y]:
                    
                    left = list(target[:i])
                    left.append(chr(y + ord('a')))

                
                    remaining = half_cnt[:]

                    for ch in left:
                        remaining[ord(ch) - ord('a')] -= 1

                    for c in range(26):
                        if remaining[c] > 0:
                            left.extend([chr(c + ord('a'))] * remaining[c])

                    left = ''.join(left)

                    return make_palindrome(left)

        return ""
