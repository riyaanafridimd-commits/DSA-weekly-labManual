'''n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
n= int(input("enter number of rows"))
num=1
for i in range (1,n+1):
       for j in range(1,i+1):
           print(num,end="")
           num=+1
       print()
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(j+1, end=" ")
    print()
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    ch=65
    for j in range(i):
        print(chr(ch), end=" ")
        ch=ch+1
        
    print()
n = int(input("Enter number of rows: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
        
    print()
n = int(input("enter n")) 
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
n=int(input("enter number of elements"))
numbers=[]
for i in range (n):
    element= input("enter elements")
    numbers.append(element)
print("list",numbers)'''
days=["monday","tuesday","wednessday","thursday","friday","saturday","sunday"]
temp=[]
for day in days:
    t=float(input("enter temperature in celsius for "+day+":"))
    temp.append(t)
max_temp=max(temp)
min_temp=min(temp)
print("Maximum temperature:",max_temp)
print("recorded on"+days[temp.index(max_temp)])
print("Minimum temoerature:",min_temp)
print("recorded on",+days[temp.index(min_temp)])




    
       
       
