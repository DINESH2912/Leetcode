class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():  # If it's an opening bracket, push onto stack
                stack.append(char)
            elif char in mapping.keys():  # If it's a closing bracket
                if not stack:
                    return False  # Unbalanced - no opening bracket to match
                top = stack.pop()
                if mapping[char] != top:
                    return False  # Brackets don't match
            else:
                return False  # Character is neither opening nor closing bracket

        return len(stack) == 0  # True if all brackets were matched and removed
