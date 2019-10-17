class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        test = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        #翻译单词
        words_t = []
        for item in words:
            temp = ''
            for i in item:
                temp += test[ord(i)-97]
            words_t.append(temp)
         #统计不同单词翻译的数量
        count = 0
        words_cnt = []
        for item in words_t:
            if item not in words_cnt:
                words_cnt.append(item)
                count += 1
        return count