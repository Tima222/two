#Вычислить сумму и произведение положительных элементов заданной прямоугольной матрицы.

n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
counter1=0
counter2=1
for i in a:
    for j in i:
        if j>0:
            counter1+=j
            counter2*=j
print("Сумма",counter1,"произведение",counter2)
