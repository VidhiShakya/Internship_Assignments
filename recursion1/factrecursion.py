
def fact_rec(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact_rec(n-1)
    
x= int(input("Enter a number: "))
print(f"The factorial is {fact_rec(x)}")

