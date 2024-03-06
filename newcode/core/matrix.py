class Matrix:
    def __init__(self, colums: int, rows: int) -> None:
        self.matrix = Matrix.createNewMatrix(colums, rows)
        self.matrixDimensions = [colums, rows]
                
    @staticmethod
    def createNewMatrix(colums, rows, value: int = 0):
        matrix = []
        for i in range(rows):
            matrixRow = []
            for j in range(colums):
                matrixRow.append(value)
            matrix.append(matrixRow)
        return matrix
    
    def eraseMatrix(self):
        self.matrix = Matrix.createNewMatrix(*self.matrixDimensions)
        
    def setMatrix(self, newMatrix):
        self.matrix = newMatrix  
    