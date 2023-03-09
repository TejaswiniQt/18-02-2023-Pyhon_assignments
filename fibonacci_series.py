#Fibonacci series


def fibonacci(n):
    num1 = 0
    num2 = 1
    print("Fibonacci series are: ")
    print(num1,num2,sep="\n")
    for i in range(n-2):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(num3,sep=" ")
    


n = int(input("Enter the number of fibonacci series to be printed : "))
fibonacci(n)
