#Программа для решения матричных уравнений
#Реализован метод крамера
class matrix:
    
    def __init__(self,lines,column):
        self.lines = lines
        self.column = column
        self.mx = []
        if lines == column:
            self.deta = 1
        else:
            self.deta = 0
            
            
    def method_kramera(self):
        deta = []
        for k in range(self.column):
            temp = matrix(self.lines,self.column - 1)
            temp.input_matrix(self.mx,k)
            temp.make_treeangle()
            deta.append(temp.deta)
        for i in range(len(deta) - 1):
            try:
                deta[i] = deta[i]/deta[self.column - 1]
            except(ZeroDivisionError):
                print("Детерминант матрицы равен нулю:/")
            print("x",i + 1," = ",deta[i],sep = '')
            
            
    def make_treeangle(self):
        for k in range(self.lines):
            for j in range(k+1,self.lines):
                d = self.mx[j][k]/self.mx[k][k]
                for i in range(k,self.column):
                    self.mx[j][i] = self.mx[j][i] - d*self.mx[k][i]
                    
        if self.lines == self.column:            
            for  i in range(self.lines):
                for j in range(self.column):
                    if i == j:
                        self.deta = self.deta*self.mx[i][j]
            
            
    def transpon(self):
        if self.lines != self.column:
            print("Зачем ты транcпонируешь прямоугольную матрицу?")
        else:
            for  i in range(self.lines):
                for j in range(self.column):
                    if i<j:
                        self.mx[i][j],self.mx[j][i]=self.mx[j][i],self.mx[i][j]
                        
    
            
    def input_matrix(self , matrix = None , k = None):
        if matrix == None:
            check = False
            for i in range(self.lines):
                self.mx.append([])
            for i in range(self.lines):
                for j in range(self.column):
                    check = False
                    while check == False:
                        try:
                            print("a[",i + 1,"][",j + 1,"]= ",sep = '',end = '')
                            input_int = int(input())
                            check = True
                        except(TypeError,ValueError):
                            print("4to ti BBel?")
                    self.mx[i].append(input_int)
        else:
            for i in range(self.lines):
                self.mx.append([])
            for i in range(self.lines):
                for j in range(self.column + 1):
                    if j != k:
                        self.mx[i].append(matrix[i][j])
                
                
                
                
    def show_matrix(self):
        if self.lines  < self.column:
            print("+",(self.column - 1)*"-------+",".......\\",sep ='')
        else:
            print("+",(self.column)*"-------+",sep ='')
        for i in range(self.lines):
            for j in range(self.column):
                print("|", '{:^6.1f}'.format(self.mx[i][j]),end = '')
            print("|\n",end = '')
        if self.lines  < self.column:
            print("+",(self.column - 1)*"-------+","'''''''/",sep ='')
        else:
            print("+",(self.column)*"-------+",sep ='')
            
def check_in():            
    check = False
    while check == False:
        try:
            print("Колличество строк: ",sep = '',end = '')
            input_int = int(input())
            check = True
        except(TypeError,ValueError):
            print("4to ti BBel?")
    return input_int
        

def __main__():
    dim = check_in()
    matr = matrix(dim , dim + 1)
    print("Введи расширенную матрицу для её решения")
    matr.input_matrix()
    matr.show_matrix()
    matr.method_kramera()
__main__()
#####DUBUG
#matr = matrix(3,3)
#matr.input_matrix()
#matr.show_matrix()
##matr.transpon()
#matr.method_kramera()
##matr.make_treeangle()
#matr.show_matrix()
##print("determinant = ","%.1f" % matr.deta)
##4  5  6  7  3  
##2  4  5  8  9  
##0  2  1  1  3  
##4  1  5  6  7  
##8  3  4  3  4   896

    
