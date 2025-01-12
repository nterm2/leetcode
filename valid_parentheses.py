# [([]())]

# I would go through each element of the string.
# Look at the next value, if it is not the same bracket, move on
# Otherwise remove the chars in those two indexes
# start again.
# otherwise if go through first iteration and no removes have been made, 
# return false.
# issue is that when front and back pointer stay the same. in reality 

class Solution:
    def isValid(self, s: str) -> bool:
        front_pointer, back_ponter = 0, 1
        s = list(s)
        while (back_ponter < len(s)):
            if len(s) % 2 != 0:
                return False 
            if self.validateParentheses(s[front_pointer], s[back_ponter]):
                del s[front_pointer]
                del s[back_ponter - 1]
                front_pointer, back_ponter = 0, 1
            else:
                front_pointer += 1
                back_ponter += 1
        if len(s) == 0:
            return True
        return False
    
    def validateParentheses(self, firstChar: str, secondChar: str):
        return (
            (ord(firstChar) == 40 and ord(secondChar) == 41) or 
            (ord(firstChar) == 91 and ord(secondChar) == 93) or 
            (ord(firstChar) == 123 and ord(secondChar) == 125) 
            )
