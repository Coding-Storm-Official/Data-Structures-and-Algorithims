#arrange digits to get max salary
arr = map(int, input().split())
arr = sorted(arr, reverse=True)
res = ''.join(map(str, arr))
print(res)