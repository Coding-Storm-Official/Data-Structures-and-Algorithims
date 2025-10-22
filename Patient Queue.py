n = int(input("Number of patients: "))
wt = []
for i in range(n):
    wt.append(int(input("Waiting time for Patient " + str(i+1) + ": ")))

wt.sort()
print("--------------------------------------------")
total_wait = 0
cumulative_wait = 0

for i in range(n):
    print("Treating patient", i+1, "with waiting time", wt[i])
    cumulative_wait += wt[i]
    total_wait += cumulative_wait
    print("Cumulative Waiting Time:", cumulative_wait)
    print("--------------------------------------------")

print("Total Minimum Waiting Time:", total_wait)
