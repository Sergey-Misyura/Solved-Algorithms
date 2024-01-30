"""
150. Evaluate Reverse Polish Notation
(Medium complexity)

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer."""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                b, a = stack.pop(), stack.pop()
                if tokens[i] == '+':
                    stack.append(a + b)
                elif tokens[i] == '-':
                    stack.append(a - b)
                elif tokens[i] == '*':
                    stack.append(a * b)
                elif tokens[i] == '/':
                    stack.append(int(a / b))

        return stack[-1]