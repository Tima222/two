#Найти наибольший элемент заданной прямоугольной матрицы и его индексы.

n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
f=a[0][0]
for i in a:
    for j in i:
        if f<j:
            f=j
for i in a:
    for j in i:
        if j==f:
            print(f,[a.index(i),i.index(f)])
