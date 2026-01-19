# program to convert infix expression into postfix expression
# infix : operator in between operands.((a + b) * c)
# prefix: operator before operands.(*A+BC) -> right to left
# postfix : operator after operands.(ab + c *)
"""
algorithm to convert prefix exp into postfix exp:
1 -> traverse through exp:
    if '(' comes push it onto the stack
    if operand comes then print it.
    if ')' then pop operators from the stack until '(' found.
2 -> if operator comes:
    push it if stack is empty or top element is '('.
    else:
    check the precedence of operator at top of stack:
    if current op is of higher precedence then push it,
    else:
    keep poping from the stack and print it until lower or equal precedence op or '(' is found then push the current op.
"""

from stack import Stack
import parentheses_checker


# helper function
def get_operator_info(opr):
    if opr == '+' or opr == '-':
        return {'precedence': 1, 'associativity': 'left'}
    elif opr == '*' or opr == '/':
        return {'precedence': 2, 'associativity': 'left'}
    elif opr == '^':
        return {'precedence': 3, 'associativity': 'right'}
    else:
        return {'precedence': 0, 'associativity': None}


def infix_to_postfix(input_str):
    my_stack = Stack()
    output = ''
    input_str = input_str.replace(' ', '')  # for removing white spaces

    if not parentheses_checker.check_parentheses(input_str):  # checking order and sequence of parentheses
        return 'exp is invalid'

    i = 0
    while i < len(input_str):
        char = input_str[i]
        if '0' <= char <= '9':  # Check for digits
            num_str = ''
            while i < len(input_str) and '0' <= input_str[i] <= '9':
                num_str += input_str[i]
                i += 1
            output += num_str
            i -= 1
        elif 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
            output += char
        elif char in '([{':
            my_stack.push(char)
        elif char in ')]}':
            while not my_stack.is_empty() and my_stack.peek() not in '([{':
                output += my_stack.pop()
            if not my_stack.is_empty() and my_stack.peek() == '(':
                my_stack.pop()
        else:
            op_info = get_operator_info(char)
            if op_info['precedence'] > 0:
                curr_precedence = op_info['precedence']
                # curr_associativity = op_info['associativity']

                while (not my_stack.is_empty() and
                       my_stack.peek() not in '([{'):
                    stack_op = my_stack.peek()
                    stack_op_info = get_operator_info(stack_op)
                    stack_precedence = stack_op_info['precedence']
                    stack_associativity = stack_op_info['associativity']

                    # For left-associative operators, pop if stack_precedence >= current_precedence
                    # For right-associative operators, pop if stack_precedence > current_precedence
                    if (stack_associativity == 'left' and stack_precedence >= curr_precedence) or \
                            (stack_associativity == 'right' and stack_precedence > curr_precedence):
                        output += my_stack.pop()
                    else:
                        break  # current op has higher precedence or is right associative with equal precedence
                my_stack.push(char)
            else:
                return 'exp is invalid'
        i += 1

    while not my_stack.is_empty():
        output += my_stack.pop()

    return output


def infix_to_prefix(input_str):
    reversed_str = ''
    for char in reversed(input_str):  # reversing input string and replacing '(' with ')' and vice versa.
        if char == '(':
            reversed_str += ')'
        elif char == ')':
            reversed_str += '('
        else:
            reversed_str += char

    # return reversed_str
    output = ''
    for char in reversed(
            infix_to_postfix(reversed_str)):  # applying same infix to postfix algorithm and reversing final output.
        output += char

    return output


if __name__ == '__main__':
    st = '(a + b) * c'
    print(infix_to_prefix(st))
    print(f"'A+B' -> {infix_to_postfix('A+B')}")
    print(f"'A+B*C' -> {infix_to_postfix('A+B*C')}")
    print(f"'(A+B)*C' -> {infix_to_postfix('(A+B)*C')}")
    print(f"'A*(B+C)' -> {infix_to_prefix('A*(B+C)')}")
    print(f"'A*B+C*D' -> {infix_to_postfix('A*B+C*D')}")
    print(f"'A+B-C' -> {infix_to_postfix('A+B-C')}")
    print(f"'A-B/C+D*E-A*C' -> {infix_to_postfix('A-B/C+D*E-A*C')}")
    print(f"'a+b*c+(d*e+f)*g' -> {infix_to_postfix('a+b*c+(d*e+f)*g')}")
    print(f"'a+b*c+(d*e+(f)*g)' -> {infix_to_postfix('a+b*c+(d*e+f)*g)')}")
    print(f"'(10+5)-2*3' -> {infix_to_postfix('(10+5)-2*3')}")
    print(f"'A^B*C' -> {infix_to_postfix('A^B*C')}")  # Test with new operator
    print(f"'A*B^C' -> {infix_to_postfix('A*B^C')}")  # Test with new operator
    print(f"'A^B^C' -> {infix_to_postfix('A^B^C')}")  # Test with right associativity
    print(infix_to_prefix('A^B^C'))
