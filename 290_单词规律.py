class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern and not s:return True
        elif not pattern or not s:return False
        hashmap = {}
        temp = s.split()
        if len(temp) != len(pattern):return False
        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                if temp[i] in hashmap.values():
                    return False
                hashmap[pattern[i]] = temp[i]
            elif pattern[i] in hashmap and hashmap[pattern[i]] != temp[i]:
                return False
        return True