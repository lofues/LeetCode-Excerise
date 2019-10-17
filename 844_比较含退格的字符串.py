class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if S == '#' and T == '#':
            return True
        s_list,t_list = list(S),list(T)
        s_stack,t_stack = [],[]
        while s_list:
            x = s_list.pop(0)
            if x == '#' and not s_stack:
                pass
            elif x == '#' and s_stack:
                s_stack.pop()
            else:
                s_stack.append(x)
        while t_list:
            x = t_list.pop(0)
            if x == '#' and not t_stack:
                pass
            elif x == '#' and t_stack:
                t_stack.pop()
            else:
                t_stack.append(x)
        return ''.join(str(x) for x in s_stack) == ''.join(str(x) for x in t_stack)