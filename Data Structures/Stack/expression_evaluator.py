# program to evaluate postfix expression
"""
algorithm to evaluate:
1. scan the expression from left to right
2. if operands come push it onto stack.
3.if operator comes then take top two operands from the stack and calculate result with current operator and push result
back to stack.
4.return the last element of stack
"""

from stack import Stack
import expression_converter

my_stack = Stack()


def postfix_evaluator(input_exp):
    input_postfix_exp = expression_converter.infix_to_postfix(input_exp)
    for char in input_postfix_exp:
        if char in '+-*/^':
            second_opnd = int(my_stack.pop())
            first_opnd = int(my_stack.pop())
            if char == '+':
                result = first_opnd + second_opnd
                my_stack.push(result)
            elif char == '-':
                result = first_opnd - second_opnd
                my_stack.push(result)
            elif char == '*':
                result = first_opnd * second_opnd
                my_stack.push(result)
            elif char == '/':
                result = first_opnd / second_opnd
                my_stack.push(result)
            else:
                result = first_opnd ** second_opnd
                my_stack.push(result)
        else:
            my_stack.push(char)

    if not my_stack.is_empty():
        return my_stack.pop()
    else:
        return 'invalid exp'


if __name__ == '__main__':
    input_s = '(3+5)-2*3'
    print(postfix_evaluator(input_s))
