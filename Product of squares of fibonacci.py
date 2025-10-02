m = int(input("M: "))
n=int(input("N: "))

# partial sum = F(n+2) - F(m+1)

def fib(a):
    arr =[0,1]
    for i in range(2,a+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[a]
    
psum = fib(n+2)-fib(m+1)
print("Partial sum = "+str(psum))
print("Last digit of partial sum: " + str(psum%10))