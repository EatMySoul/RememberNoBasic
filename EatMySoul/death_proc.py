#Это макет того как не надо делать
#Тут я решил юзануть классы
#Тут я плохо юзанул классы:/
import os
class matrix:
    
    
    
    def __init__(self,lines,column):
        self.lines = lines
        self.column = column
        self.mx = []
        if lines == column:
            self.dim = lines
            self.deta = 1
        else:
            self.deta = 0
            
            
            
            
    def get_NxM_matrix(self): #Метод должен из костыля, в виде одномерного массива, сделать двумерный
        matrix = []           #Если убрать костыль, этот метод становится бесполезным
        k = 0            
        for i in range(self.lines):
            matrix.append([])
        for i in range(self.lines):
            for j in range(self.column):
                matrix[i].append(self.mx[k])
                k = k + 1
        return matrix
    
    
    
    
    def get_treeange_matrix(self):
        matrix = self.get_NxM_matrix() 
            
        for k in range(self.lines):
            for j in range(k+1,self.lines):
                d = matrix[j][k]/matrix[k][k]
                for i in range(k,self.column):
                    matrix[j][i] = matrix[j][i] - d*matrix[k][i]
                    
        k = 0
        for  i in range(self.lines):    #Это преобразование двумерного массива в одномерный костыль
            for j in range(self.column):
                if i == j and self.lines == self.column:
                    self.deta = self.deta*matrix[i][j]
                self.mx[k] = matrix[i][j]
                k = k + 1
    
            
    def transpon(self):
        a = []
        k = 0
        #появилось из-за одномерного массива ->
        for i in range(self.column):  
            a.append([])
        for i in range(self.lines):
            for j in range(self.column):
                a[i].append(self.mx[k])
                k = k + 1
        #появилось из-за одномерного массива <-
        k = 0
        for  i in range(self.lines):
            for j in range(self.column):
                if i<j:
                    a[i][j],a[j][i]=a[j][i],a[i][j]
        #появилось из-за одномерного массива ->
        for  i in range(self.column):
            for j in range(self.column):
                self.mx[k] = a[i][j]
                k = k + 1
        #появилось из-за одномерного массива <-
            
            
    def matrix_input(self):
        for i in range(self.lines*self.column):
            self.mx.append(int(input()))
            
            
    def show(self , matrix = None , dim = None):  #Вывод просто кривой
        
        #Hy}|{Ho
        if matrix == None:
            matrix = self.mx
            dim = self.column
        #u|lu HET?
            
        for i in range(len(matrix)):
            if i % dim == 0:
                print()
            print(matrix[i]," ", end ='')
        print()
        
            
            
matr = matrix(5,5)
matr.matrix_input()
matr.show()
#matr.transpon()
matr.get_treeange_matrix()
matr.show()
print("determinant=", matr.deta)
#4  5  6  7  3  
#2  4  5  8  9  
#0  2  1  1  3  
#4  1  5  6  7  
#8  3  4  3  4   896
#  4  5  8  9  
#  2  1  1  3  
#  1  5  6  7  
#  3  4  3  4  -84
#1  1  3
#5  6  7
#4  3  4  -16
        
    
