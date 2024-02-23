class Solution(object):
    def removeOuterParentheses(self, s):
        result = []
        open_count = 0
        for char in s:
            if char == '(':
                if open_count > 0:  # Skip the outermost opening parenthesis
                    result.append(char)
                open_count += 1
            elif char == ')':
                open_count -= 1
                if open_count > 0:  # Skip the outermost closing parenthesis
                    result.append(char)

        return ''.join(result)
                        