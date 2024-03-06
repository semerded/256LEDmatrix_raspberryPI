class Matrix:
    def __init__(self, colums: int, rows: int) -> None:
        self.matrix = Matrix.makeEmptyMatrix(colums, rows)
        self.matrixDimensions = [colums, rows]
                
    @staticmethod
    def makeEmptyMatrix(colums, rows, value: int = 0):
        matrix = []
        for i in range(rows):
            matrixRow = []
            for j in range(colums):
                matrixRow.append(value)
            matrix.append(matrixRow)
        return matrix
    
    def eraseMatrix(self):
        self.matrix = Matrix.makeEmptyMatrix(*self.matrixDimensions)
        
    def setMatrix(self, newMatrix):
        self.matrix = newMatrix  
    