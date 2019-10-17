class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1 = 'QWERTYUIOPqwertyuiop'
        line2 = 'ASDFGHJKLasdfghjkl'
        line3 = 'ZXCVBNMzxcvbnm'
        for index in range(len(words)):
            cnt1 = cnt2 = cnt3 = 0
            for c in words[index]:
                    if c in line1:
                        cnt1 += 1
                    elif c in line2:
                        cnt2 += 1
                    elif c in line3:
                        cnt3 += 1
            if cnt1 == len(words[index]) or cnt2 == len(words[index]) or cnt3 == len(words[index]):
                pass
            else:
                words[index] = ''
        return [key for key in words if key != '']