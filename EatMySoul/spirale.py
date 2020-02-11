
def smart_in():            
    check = False
    while check == False:
        try:
            input_int = int(input())
            if input_int > 2:
                check = True
            else:
                print("\033[31m","[!]","\033[0m Некоректное значение")
        except(TypeError,ValueError):
            print("\033[31m","[!]","\033[0m Некоректное значение")
    return input_int

def main():
    print ("Пиши число: ", end = '')
    num = smart_in()
    a = []
    m = 1
    for i in range(num + 1):
        a.append([])
    for i in range(num + 1):
        for j in range(num + 1):
            a[i].append(1)
    if num % 2 != 0:
        tmp = num // 2
        a[tmp][tmp] = num*num
    for k in range(num - 2):
        i_min = k 
        i_max = num - k - 1
        for i in range(k,num - 1 - k):
            a[i_min][i] = m
            m = m + 1
        for i in range(k,num - 1 - k):
            a[i][i_max] = m
            m = m + 1
        for i in range(num - 1 - k , k , -1):
            a[i_max][i] = m
            m = m + 1
        for i in range(num - 1 - k ,k , -1):
            a[i][i_min] = m
            m = m + 1
    for i in range(num):
        for j in range(num):
            print ('{:^4.0f}'.format(a[i][j]),end = ' ')
        print("\n")
main()
