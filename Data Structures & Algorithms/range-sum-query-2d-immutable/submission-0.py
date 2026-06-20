class NumMatrix:
    matrix = []
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        n = row1
        sumVal = 0
        while n <= row2 :
            sumVal += sum(self.matrix[n][col1 : col2 + 1])
            n += 1
        return sumVal
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)