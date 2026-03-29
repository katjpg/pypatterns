class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == "+":
                stack.append(stack.pop() + stack.pop())
            elif ch == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif ch == "*":
                stack.append(stack.pop() * stack.pop())
            elif ch == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(ch))

        return stack.pop()


"""
time: O(n)
- each token pushed/popped at most once.
- all arithmetic + stack operations are O(1).

space: O(n)
- stack holds at most n/2 operands at any point.

"""
