class Solution(object):
    def decodeString(self, s):
        stack = []
        
        for char in s:
            if char.isdigit():  # If the character is a digit
                if stack and stack[-1].isdigit():
                    stack[-1] += char  # Append to the last element in stack
                else:
                    stack.append(char)  # Start a new number
            elif char.isalpha():  # If the character is a letter
                if stack and stack[-1].isalpha():
                    stack[-1] += char  # Append to the last element in stack
                else:
                    stack.append(char)  # Start a new letter
            elif char == '[':  # If the character is '['
                stack.append('')  # Push an empty string as a placeholder for the bracket
            elif char == ']':  # If the character is ']'
                temp = ''  # Temporary variable to store the content of the bracket
                while stack[-1].isalpha():
                    temp = stack.pop() + temp  # Build the string inside the bracket
                stack.pop()  # Remove the '['
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num  # Get the multiplier
                stack.append(int(num) * temp)  # Multiply the string inside the brackets with the number
        
        return ''.join(stack)

