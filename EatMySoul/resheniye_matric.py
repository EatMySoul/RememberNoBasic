#Программа для решения матричных уравнений
#Реализован метод крамера и гауса
import random


class matrix:
    
    def __init__(self,lines,column):
        self.lines = lines
        self.column = column
        self.mx = []
        self.deta = 1
            
        
    def method_gausa(self):
        temp = matrix(self.lines,self.column)
        temp.mx = self.mx
        temp.make_treeangle()
        temp.show_matrix()
        temp.gaus()
        
            
            
    def method_kramera(self):
        deta = []
        for k in range(self.column):
            temp = matrix(self.lines,self.column - 1)
            temp.input_matrix(self.mx,k)
            temp.show_matrix()
            temp.make_treeangle()
            print("Детерминант матрицы: = ","%.2f" % temp.deta,"\n\n")
            deta.append(temp.deta)
        for i in range(len(deta) - 1):
            try:
                deta[i] = deta[i]/deta[self.column - 1]
            except(ZeroDivisionError):
                print("Детерминант матрицы равен нулю")
                break
            print("x",i + 1," = ",deta[i],sep = '')
            
          
          
    def make_treeangle(self):
        for k in range(self.lines):
            for j in range(k+1,self.lines):
                if self.mx[k][k] != 0:
                    d = self.mx[j][k]/self.mx[k][k]
                else:
                    d = 0
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
                        
    
            
    def input_matrix(self , matrix = None , column = None , line = None):
        if matrix == None:
            check = False
            for i in range(self.lines):
                self.mx.append([])
            for i in range(self.lines):
                for j in range(self.column):
                    check = False
                    while check == False:
                        try:
                            if (j + 1) < self.column:
                                print("x",j + 1,"*",sep = '',end = '')
                            else:
                                print("b",i+1," = ",sep = '',end = '')
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
                    if j != column and i != line:
                        self.mx[i].append(matrix[i][j])
                        
                        
    def gaus(self):
        x = []
        if self.column > self.lines + 1:
            print("Уравнение имеет бесконечное колличество решений")
            for i in range(self.column):
                x.append(1)
            for i in range(self.lines + 1,self.column):
                print("Переменная x",i," является базисной, Введите её значение: ",end = '', sep = '')
                x[i - 1] = check_in()
            for k in range(self.lines - 1,-1,-1):
                d = 0
                for j in range(k + 1,self.column - 1):
                    d = d - self.mx[k][j]*x[j]
                    x[k] = (d + self.mx[k][self.column - 1])/self.mx[k][k]
            print("Возможное решение:")
        else:
            for i in range(self.column):
                x.append(1)
            for k in range(self.lines - 1,-1,-1):
                d = 0
                for j in range(k + 1,self.column - 1):
                    d = d - self.mx[k][j]*x[j]
                x[k] = (d + self.mx[k][self.column - 1])/self.mx[k][k]
        for i in range(len(x) - 1):
            print ("x",i + 1," = ", '%.1f' % x[i] , sep = '')
        
                
                
                
                
    def show_matrix(self):
        if self.lines  < self.column:
            print("\n+",(self.column - 1)*"-------+",".......\\",sep ='')
        else:
            print("+",(self.column)*"-------+",sep ='')
        for i in range(self.lines):
            for j in range(self.column):
                print("|", '{:^6.1f}'.format(self.mx[i][j]),end = '')
            print("|\n",end = '')
        if self.lines  < self.column:
            print("+",(self.column - 1)*"-------+","'''''''/","\n\n",sep ='')
        else:
            print("+",(self.column)*"-------+","\n\n",sep ='')
            
            
            
def check_in():            
    check = False
    while check == False:
        try:
            input_int = int(input())
            check = True
        except(TypeError,ValueError):
            print("4to ti BBel?")
    return input_int
        


def __main__():
    print("Колличество строк: ",sep = '',end = '')
    lines = check_in()
    column = 0
    while lines  >= column:
        print("Колличество переменных: ",sep = '', end = '')
        column = check_in()
    matr = matrix(lines , column + 1)
    print("Введи расширенную матрицу для её решения")
    matr.input_matrix()
    matr.show_matrix()
    temp = matr
    temp.make_treeangle()
    if temp.deta != 0:
        if lines + 1 == column:
            print("Метод решения:\n[ 1 ]Метод гауса\n[ 2 ]Метод крамера\nВыбирай с умом: " , end = '')
            chose = check_in()
            if chose == 1:
                matr.method_gausa()
            else:
                matr.method_kramera()    
        else:
            matr.method_gausa()
    else:
        print("У этой матрицы нет решений")
__main__()


    
