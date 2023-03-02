class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to be added")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to be subtracted")
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[self.matrix[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result)
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix")
            result = [[sum([self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)]) for j in range(other.cols)] for i in range(self.rows)]
            return Matrix(result)
        else:
            raise TypeError("Multiplication is only defined for a matrix and a scalar or two matrices")

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(result)

    @staticmethod
    def from_list(lst):
        return Matrix(lst)

    def to_list(self):
        return self.matrix

    def to_row_list(self):
        return self.matrix.copy()




m1 = Matrix([[7, 0, 8, 8, 8], [0, 0, 1, 3, 5], [0, 0, 0, -3, 5], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
m2 = Matrix([[2, 1], [-3, 0], [4, -1]])
m3 = Matrix([[5, -1, 6], [-3, 0, 7]])

# Matrix multiplication to number
m4 = m1 * 4
print("Matrix 1 * 4:")
print(m4)

# Matrix multiplication
m5 = m2 * m3
print("Matrix 2 * Matrix 3:")
print(m5)
