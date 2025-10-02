#My approach - O(min(a,b)) [Brute-force] 
a=int(input("A: "))
b=int(input("B: "))
fc = max(a,b)
fcd = []
ans = 1
for i in range(1,fc):
    if fc%i==0 and i<=b:
        fcd.append(i)

for i in range(len(fcd)):
    if b%fcd[i]==0:
        ans = max(ans,fcd[i])

print(ans)



#Euclidean algorithm - O(log(min(a,b)))
a = int(input())
b = int(input())
while b:
    a, b = b, a % b
print(a)

