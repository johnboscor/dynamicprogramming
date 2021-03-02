#Find min weight to get max value

def knapsack(max_val, wt, val,n):
    if n == 0 or max_val <= 0:
        return 0

    else:
        return max(wt[n-1] + knapsack(max_val-val[n-1],wt,val,n-1),knapsack(max_val,wt,val,n-1))

val = [60, 100, 120]
wt = [10, 20, 30]
max_val = sum(val)
n = len(val)
#dp = [[-1 for i in range(TW +1 )] for _ in range(n +1 )]
#print(dp)
print(knapsack(max_val,wt,val,n))