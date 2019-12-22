def instruction():
	print('''Какую операцию вы хотите совершить над массивом:
	1.Найти сумму и количество положительных элементов массива.
	2.Найти элемент массива и его порядковый номер.
	3.Найти максимальный элемент массива и его порядковый номер.
	4.Найти минимальный элемент массива.
	5.Найти сумму и количество положительных элементов, 
	расположенных между минимальным и максимальным элементами. 
	6.Упорядочить элементы, массива по убыванию. 
	7.Упорядочить элементы, массива по возрастанию.
	8.Определить количество отрицательных элементов. 
	9.Определить количество положительных элементов.
	10.Найти количество нечетных положительных элементов. 
	11.Найти количество четных положительных элементов.
	12.Найти сумму четных положительных элементов. 
	13.Найти сумму нечетных положительных элементов. 
	14.Найти произведение положительных элементов. 
	15.Найти определить количество элементов, равных 4.
	16.Даны массивы А(5) и В(10). Вычислить разность соответствующих.
	17.Определить количество элементов, меньших 4.
	18.Вычислить произведение отрицательных элементов массивов.
	19. Найти наименьший положительный элемента среди элементов с четными номерами массива
	20.Найти наибольший среди элементов массива А(10), остальные обнулить.
''')
def operation1(mass,num):
	total=0
	k=0
	for i in range(num):
		if mass[i]>0:
			total=total+mass[i]
			k+=1

	print('Сумма=',total);print('количество:',k)
def operation2(mass):
	numb=int(input('Какой элемент вы хотите найти:'))
	if numb not in mass:
		print ('Такого элемента нет в массиве.')
	else:
		Index=mass.index(numb)
		print ('нужный элемент под индексом ',Index)
def operation3(mass):
	Max=max(mass)
	Index=mass.index(Max)
	print('Максимальный элемент=',Max,'с индексом',Index)
def operation4(mass):
	Min=min(mass)
	Index=mass.index(Min)
	print('Минимальный элемент=',Min,'с индексом',Index)
def operation5(mass):
	total=0
	Min=min(mass)
	Index1=mass.index(Min)
	Max=max(mass)
	Index2=mass.index(Max)
	if Index1 > Index2:
		Index1,Index2=Index2,Index1
	for i in range (Index1+1,Index2):
		total=total+mass[i]
	print('Сумма=',total)
def operation6(mass,num):
	for j in range(0,num-1):
		for i in range(0,num-1):
			if mass[i]<mass[i+1]:
				mass[i],mass[i+1]=mass[i+1],mass[i]
	print(mass)
def operation7(mass,num):
	for j in range(0,num-1):
		for i in range(0,num-1):
			if mass[i]>mass[i+1]:
				mass[i],mass[i+1]=mass[i+1],mass[i]
	print(mass)
def operation8(mass,num):
	k=0
	for i in range(num):
		if mass[i]<0:
			k+=1
	print('количество:',k)
def operation9(mass,num):
	k=0
	for i in range(num):
		if mass[i]>0:
			k+=1
	print('количество:',k)
def operation10(mass,num):
	k=0
	for i in range(num):
		if mass[i]%2 !=0 and mass[i]>0:
			k+=1
	print('количество:',k)
def operation11(mass,num):
	k=0
	for i in range(num):
		if mass[i]%2 ==0 and mass[i]>0:
			k+=1
	print('количество:',k)
def operation12(mass,num):
	total=0
	for i in range(num):
		if mass[i]>0 and mass[i] %2==0:
			total+=mass[i]
	print('Сумма=',total)
def operation13(mass,num):
	total=0
	for i in range(num):
		if mass[i]>0 and mass[i] %2 !=0:
			total+=mass[i]
	print('Сумма=',total)
def operation14(mass,num):
	production=0
	for i in range(num):
		if mass[i]>0:
			production+=mass[i]
	print('произведение=',production)
def operation15(mass,num):
	k=0
	Index=[]
	for i in range(num):
		if mass[i]==4:
			k+=1
			Index.append(i)
		else:
			print('В массиве нет элементов равных 4')
			
			
	print('количество:',k)
	print('С индексами',Index)
def operation16(massA,massB,num):
	total=0
	C=[]
	for i in range(num):
		x=massA[i]-massB[i]
		C.append(x)
	print(C)
def operationt17(mass,num):
	k=0
	for i in range(num):
		if mass[i]<4:
			k+=1
	print('количество:',k)
def operation18(mass,num):
	production
	for i in range(num):
		if mass[i]<0:
			production*=mass[i]
	print ('произведение=',production)
def operation19(mass,num):
	c=[]
	for i in range(num):
		if mass[i]>0:
			c.append(mass[i])
	Min=min(c)
	In=mass.index(Min)
	print ('Минимальный элемент:',Min,',С индексом',In+1)
def operation20(mass,num):
	Max=max(mass)
	In=mass.index(Max)
	for i in range(num):
		mass[i]=0
	mass.insert(In,Max)
	print(mass)





instruction()#НАЧАЛО
oper=int(input('операция:'))
a=[]
b=[]

if oper==16:# Т.к здесь операции с 2-мя массивами вынесим отдельно эту функцию
	N1=int(input('Введите размерность массива A:'))
	for i in range(N1):
		print('a',i+1,':',end='')
		numb=int(input())
		a.append(numb)

	N2=int(input('Введите размерность массива B:'))
	for i in range(N2):
		print('b',i+1,':',end='')
		numb=int(input())
		b.append(numb)

	n=min(N1,N2)
	
else:
	n=int(input('Введите размерность матрицы:'))
	print ('Введите элементы матрицы')
	for i in range(n):
		print('a',i+1,':',end='')
		numb=int(input())
		a.append(numb)


if oper==1:
	operation1(a,n)
if oper==2:
	operation2(a)
if oper==3:
	operation3(a)
if oper==4:
	operation4(a)
if oper==5:
	operation5(a)
if oper==6:
	operation6(a,n)
if oper==7:
	operation7(a,n)
if oper==8:
	operation8(a,n)
if oper==9:
	operation9(a,n)
if oper==10:
	operation10(a,n)
if oper==11:
	operation11(a,n)
if oper==12:
	operation12(a,n)
if oper==13:
	operation13(a,n)
if oper==14:
	operation14(a,n)
if oper==15:
	operation15(a,n)
if oper==16:
	operation16(a,b,n)
if oper==17:
	operation17(a,n)
if oper==18:
	operation18(a,n)
if oper==19:
	operation19(a,n)
if oper==20:
	operation20(a,n)


input()