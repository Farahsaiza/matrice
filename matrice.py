
R=int(input("enter  the number of rows: "))
C=int(input("enter  the number of columns: "))
T1=[]
X=0
for i in range (R):
    T2=[]
    for j in range(C):
        X=X+1
        
        T2.append(X)
    if  i % 2 ==  0:
        print(T2)
    else:
       print(T2[::-1])

    T1.append(T2)

    

    






