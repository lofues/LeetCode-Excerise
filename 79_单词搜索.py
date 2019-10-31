class Solution:
    directions = [(0,-1),(1,0),(0,1),(-1,0)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.__search_word(board,marked,word,i,j,0,m,n):
                    return True
                print(marked)
        return False
    
    def __search_word(self,board,marked,word,start_x,start_y,index,m,n):
        # 递归搜索终止条件
        if index == len(word)-1:
            return word[index] == board[start_x][start_y]
        # 中间搜索
        if board[start_x][start_y] == word[index]:
            # 先占据该位置
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y] and self.__search_word(board,marked,word,new_x,new_y,index+1,m,n):
                    return True
            marked[start_x][start_y] = False
        return False