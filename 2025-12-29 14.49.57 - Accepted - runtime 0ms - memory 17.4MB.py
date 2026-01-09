class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # Count frequencies and check if all diffs <= 3
        # Time: O(n), Space: O(1) - 26 chars max
        from collections import Counter
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        # Check all letters a-z
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if abs(count1.get(c, 0) - count2.get(c, 0)) > 3:
                return False
        return True