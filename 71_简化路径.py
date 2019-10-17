def simplifyPath( path: str) -> str:
    tmp = re.split(r'/+', path)
    tmp = [x for x in tmp if x and x != '.']
    if not tmp: return '/'
    stack = []
    while tmp:
        x = tmp.pop(0)
        if x == '..':
            if stack:
                stack.pop()
        else:
            stack += [x]
    return '/' + '/'.join(stack)

print(simplifyPath("/a//b////c/d//././/.."))
print(simplifyPath("/a/../../b/../c//.//"))