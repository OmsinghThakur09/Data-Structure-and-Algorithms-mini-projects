# program to check sequence and order of all types of brackets in expression, basically the functions takes
# expression as input string and returns true if sequence is proper otherwise false.

from stack import Stack

my_stack = Stack()


def check_parentheses(input_str):
    my_stack = Stack()
    mapping = {'}': '{', ')': '(', ']': '['}
    for char in input_str:
        if char in '([{':
            my_stack.push(char)
        elif char in ')]}':
            if my_stack.is_empty():
                return False  # closing parentheses without a matching opening one
            top = my_stack.pop()
            if mapping[char] != top:
                return False  # mismatched parentheses

    return my_stack.is_empty()  # true if all matched and stack is empty false otherwise


if __name__ == '__main__':
    st = 'a+b*c+(d*e+f)*g)'
    print(check_parentheses(st))
