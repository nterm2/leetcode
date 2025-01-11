# can use two pointers
# iterate through each character. 
# if front pointer is equal to back pointer, return true
# otherwise, while difference between back pointer and front pointer is not negative, carry on

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower())


        s = ''.join(char.lower() for char in s if char.isalnum())
        front_pointer = 0
        back_pointer = len(s) - 1
        while ((back_pointer - front_pointer) >= 0):
            if (back_pointer - front_pointer == 0):
                return True
            elif s[front_pointer] == s[back_pointer]:
                front_pointer += 1
                back_pointer -= 1
            else:
                return False
            
        return True 
    