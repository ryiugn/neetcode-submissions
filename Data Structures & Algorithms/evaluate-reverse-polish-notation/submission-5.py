class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in ('+', '-', '*', '/'):
                stack.append(int(ch))
            elif ch == '+':
                first = stack.pop()
                second = stack.pop()
                temp = first + second
                stack.append(temp)
            elif ch == '-':
                first = stack.pop()
                second = stack.pop()
                temp = second - first
                stack.append(temp)
            elif ch == '*':
                first = stack.pop()
                second = stack.pop()
                temp = first * second
                stack.append(temp)
            elif ch == '/':
                first = stack.pop()
                second = stack.pop()
                temp = int(second / first)
                stack.append(temp)
        return stack[0]