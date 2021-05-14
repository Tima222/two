#Вычислить сумму наибольшего и наименьшего элементов заданной прямоугольной матрицы.
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
f=a[0][0]
g=a[0][0]
for i in a:
    for j in i:
        if f<j:
            f=j
        elif g>j:
            g=j
print(f+g)
