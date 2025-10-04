#My original approach
n,k = map(int,input().split())
a = 0
kill = 1
rebels = []
for i in range(1,n+1):
    rebels.append(i)

while len(rebels)>1:
    if kill == k:
        rebels.pop(a)
        kill=1
        if a==len(rebels):
            a=0
    else:
        a+=1
        if a==len(rebels):
            a=0
        kill+=1
print("Survivor at position " + str(rebels[0]))