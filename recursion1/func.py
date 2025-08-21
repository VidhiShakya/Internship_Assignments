def func(n):
    if n==0:
        return
    else:
        print(n)
        func(n-1)

x = int(input("Enter a number: "))
func(x)