def is_balanced(s):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in brackets:
            stack.append(char)
        elif stack and char == brackets[stack[-1]]:
            stack.pop()
        else:
            return "NO"
    
    return "YES" if not stack else "NO"

# Example usage
if __name__ == "__main__":
    s = input("Enter the string of brackets: ")
    print(is_balanced(s))
