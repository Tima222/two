#Определить наибольший элемент в каждом столбце заданной прямоугольной матрицы В. Вычислить сумму элементов 3-го столбца.

n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
n=0
counter1=0
for i in a:
    print("Максимальный элемент сторки",n,"равен",max(i))
    n+=1
for i in a[2]:
    counter1+=i
print("Сумма элементов 3-ей строки",counter1)
