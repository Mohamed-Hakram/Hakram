ar=[]

n = int(input("Enter the number:\n"))
for i in range(n):
    a= input(f"Enter element {i+1}: ")
    ar.append(a)

search=input("Enter  search key:\n")
for i in range(n):
    if ar[i] == search:
        print(f"Element found at position {i + 1}")
        break
if ar[i]!=search:
        print("Not found" )

