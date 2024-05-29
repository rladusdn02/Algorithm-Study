a=int(input())
b=int(input())
c=int(input())

ct=list(str(a*b*c))

for i in range(10):
    print(ct.count(str(i)))
