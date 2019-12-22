#Это макет того как не надо делать
#Ага, это вторая версия неумения использовать классы
class matrix:
    
    def __init__(self,lines,column):
        self.lines = lines
        self.column = column
        self.mx = []
        if lines == column:
            self.dim = lines
            self.deta = 1
        else:
            self.dim = column
            self.deta = 0
            
    def get_matrix_treeangle(self,matrix = None , column = None, lines = None):
        if matrix == None:
            matrix = self.mx
        if column == None:
            column = self.column
        if lines == None:
            lines = self.lines
            
            
        matrix = self.get_twodim(matrix,column,lines)
        
        for k in range(lines):
            for j in range(k+1,lines):
                d = matrix[j][k]/matrix[k][k]
                for i in range(k,column):
                    matrix[j][i] = matrix[j][i] - d*matrix[k][i]
                    
                    
        for  i in range(lines):
            for j in range(column):
                if i == j and lines == column:
                    self.deta = self.deta*matrix[i][j]
                    
                    
        matrix = self.get_onedim(matrix,column,lines)
        return matrix
            
            
    def transpon(self,matrix = None , column = None , lines = None):
        if matrix == None:
            matrix = self.mx
        if column == None:
            column = self.column
        if lines == None:
            lines = self.lines
        if lines != column:
            print("Зачем ты транcпонируешь прямоугольную матрицу?")
            return matrix
        else:
            k = 0
            A = self.get_twodim(matrix,column,lines)
            for  i in range(lines):
                for j in range(column):
                    if i<j:
                        A[i][j],A[j][i]=A[j][i],A[i][j]
            A = self.get_onedim(A,column,lines)
            return A    
    
    
    
    def get_twodim(self,matrix = None, column = None , lines = None ):
        if matrix == None:
            matrix = self.mx
        if lines == None:
            lines = self.lines
        if column == None:
            column = self.column
        A = []
        k = 0
        for i in range(lines):
            A.append([])
        for i in range(lines):
            for j in range(column):
                A[i].append(matrix[k])
                k = k + 1
        return A
    
    def get_onedim(self,matrix , column, lines):
        A = []
        for  i in range(lines):
            for j in range(column):
                A.append(matrix[i][j])
        return A
            
    def show(self,matrix = None,dim = None):
        if matrix == None:
            matrix = self.mx
        if dim == None:
            dim = self.column
        k = 0
        print("+",dim*"---+",sep ='')
        for i in range(self.lines):
            for j in range(dim):
                print("|",matrix[k],"", end = '')
                k = k + 1
            print("|\n",end = '')
        print("+",dim*"---+",sep ='')
        
    
    def matrix_input(self):
        check = False
        for i in range(self.lines):
            for j in range(self.column):
                check = False
                while check == False:
                    try:
                        print("A[",i + 1,"][",j + 1,"]= ",sep = '',end = '')
                        input_int = int(input())
                        check = True
                    except(TypeError,ValueError):
                        print("4to ti BBel?")
                self.mx.append(input_int)
                
                
                
matr = matrix(4,4)
matr.matrix_input()
matr.show()
matr.method_kramera()
print("determinant=",matr.deta)
matr.show()
#4  5  6  7  3  
#2  4  5  8  9  
#0  2  1  1  3  
#4  1  5  6  7  
#8  3  4  3  4   896
