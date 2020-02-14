import os
def smart_in(massage = ''):            
    check = False
    while check == False:
        try:
            input_int = int(input(massage))
            check = True
        except(TypeError,ValueError):
            print("\033[31m","[!]","\033[0m Некоректное значение")
    return input_int

def q1():
    sum = 0
    mass = []
    for i in range(8):
        mass.append([])
    for i in range(8):
        for j in range(9):
            if i == 0:
                print("B(", i + 1,",",j + 1,")", end = '' , sep = '')
            else:
                print("A(", i + 1,",",j + 1,")", end = '' , sep = '')
            mass[i].append(smart_in())
    for i in range(8):
        temp_sum = 0
        for j in range(9):
            temp_sum = temp_sum + mass[i][j]*mass[0][j]*mass[0][j]
        sum = sum + temp_sum
    print(" [\033[32m+\033[0m] Sum = ",sum)
    
def q2():
    sum = 0
    mass = []
    N = smart_in("N = ")
    for i in range(N):
        print("A(",i+1,") = " ,end = '' , sep = '')
        mass.append(smart_in())
        sum = sum + mass[i]
    print(" [\033[32m+\033[0m] Sum = ",sum)
    
def q3():
    sum = 0
    mass = []
    N = smart_in("N = ")
    M = smart_in("M = ")
    for i in range(N):
        mass.append([])
    for i in range(N):
        for j in range(M):
            print("B(", i + 1,",",j + 1,")", end = '' , sep = '')
            mass[i].append(smart_in())
            sum = sum + mass[i][j]
    print(" [\033[32m+\033[0m] sum = ",sum)
    
def q4():
    A = []
    B = []
    N = smart_in("N = ")
    for i in range(N):
        print("A(", i + 1, ") = ", sep = '', end = '')
        A.append(smart_in())
    for i in range(N):
        print("B(", i + 1, ") = ", sep = '', end = '')
        B.append(smart_in())
    for i in range(N):
        sum = A[i] + B[i]
        print(" [\033[32m+\033[0m] sum = ",sum) 
        
def q5():
    A = []
    B = []
    N = smart_in("N = ")
    M = smart_in("M = ")
    for i in range(N):
        A.append([])
    for i in range(N):
        for j in range(M):
            print("A(", i + 1,",",j + 1,")", end = '' , sep = '')
            A[i].append(smart_in())
    for i in range(N):
        B.append([])
    for i in range(N):
        for j in range(M):
            print("B(", i + 1,",",j + 1,")", end = '' , sep = '')
            B[i].append(smart_in())
    for i in range(N):
        for j in range(M):
            sum = A[i][j] + B[i][j]
            print(" [\033[32m+\033[0m] sum = ",sum)

while True:
    choose = smart_in("choose your destiny: ")
    if choose == 1:
        q1()
    elif choose == 2:
        q2()
    elif choose == 3:
        q3()
    elif choose == 4:
        q4()
    elif choose == 5:
        q5()
    
    
