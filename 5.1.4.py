import math

a=[]

n = int(input("Enter the number:"))
print(n)
add=0
for i in range(n):
    e=float(input(f"Enter element{i+1}:"))
    print(e)
    a.append(e)
    add=add+e
mean=add/n
variance = sum((x- mean) ** 2 for x in a) / n
deviation = math.sqrt(variance)
print("Mean:",mean)
print("Variance:",variance)
print("Deviation:",deviation) 





