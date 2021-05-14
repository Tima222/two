#Определить наименьший элемент каждой четной строки заданной квадратной матрицы А и сумму этих элементов.

n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
n=0
counter1=0
for i in a:
    if n%2==0:
        print("Минимальный элемент строки",n,"равен",min(a[n]))
        counter1+=min(a[n])
        n+=2
    if len(a)==n or len(a)==n-1:
        break
print("Сумма миниимальных элементов равна",counter1)
