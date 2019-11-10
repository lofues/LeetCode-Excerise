class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        def helper(v1,v2):
            if not v1 and not v2:
                return 0
            elif v1 and not v2:
                v1 = set(''.join(v1))
                if len(v1) == 1 and '0' in v1:
                    return 0
                return 1
            elif not v1 and v2:
                v2 = set(''.join(v2))
                if len(v2) == 1 and '0' in v2:
                    return 0
                return -1
            if int(v1[0]) > int(v2[0]):
                return 1
            elif int(v1[0]) < int(v2[0]):
                return -1
            else:
                return helper(v1[1:],v2[1:])
        return helper(version1,version2)