class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        for char in t:
            if char not in s_list or len(s) != len(t):
                return False
            s_list.remove(char)
        return True