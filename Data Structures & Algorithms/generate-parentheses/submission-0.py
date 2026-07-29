class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def dfs(opencount, closedcount):
            if opencount == closedcount == n:
                res.append("".join(stack))
                return
            if opencount < n:
                stack.append('(')
                dfs(opencount + 1, closedcount)
                stack.pop()
            if closedcount < opencount:
                stack.append(')')
                dfs(opencount, closedcount + 1)
                stack.pop()
        dfs(0, 0)
        return res