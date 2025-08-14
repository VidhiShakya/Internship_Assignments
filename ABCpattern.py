# ABCpattern.py

n=int(input("Enter ASCII value of starting character:  "))
m=int(input("Enter ASCII value of ending character:  "))

for i in range (n,m+1):
    for j in range(n, i+1):
        print(chr(j), end="")
    print()