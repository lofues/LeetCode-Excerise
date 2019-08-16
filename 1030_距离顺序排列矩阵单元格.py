class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def get_distance(r1,c1,r0,c0):
            return abs(r1-r0) + abs(c1-c0)
        tuple_list = []
        for r in range(R):
            for c in range(C):
                tuple_list.append((r,c,get_distance(r,c,r0,c0)))
        tuple_list.sort(key=lambda x:x[2])
        result = [[r,c] for r,c,d in tuple_list]
        return result