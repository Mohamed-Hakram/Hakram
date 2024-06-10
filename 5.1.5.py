import math
a=int(input())
l=[]
d=0
e=0
print("Enter the value:",a)
print("Enter values:")
for i in range(0,a):
    b=int(input())
    l.append(b)
    s=s+b
    mean=s/a
    print("Mean:",mean)
    for i in range(0,a):
        c=c+pow(l[i]-mean,2)
        variance=c/n
        deviation=math.sqrt(variance)
        print("Variance=",variance)
        print("Deviation=",deviation)
