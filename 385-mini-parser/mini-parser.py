class Solution:
    def deserialize(self, s: str) -> 'NestedInteger':
        if not s:
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))
        stack = []
        num = ''
        for ch in s:
            if ch == '[':
                stack.append(NestedInteger())
            elif ch == ']' or ch == ',':
                if num != '' and num != '-':
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
                elif num == '-':
                    num = ''
                if ch == ']' and len(stack) > 1:
                    top = stack.pop()
                    stack[-1].add(top)
            else:
                num += ch
        return stack[0]