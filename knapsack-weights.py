#https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/?ref=lbp

def knapsack(TW, wt, val,n):
    if n == 0 or TW <= 0:
        return 0
    if dp[n][TW] != -1:
        return dp[n][TW]
    if wt[n-1] > TW:
        dp[n][TW] = knapsack(TW,wt,val,n-1)
    else:
        dp[n][TW] = max(val[n-1] + knapsack(TW-wt[n-1],wt,val,n-1),knapsack(TW,wt,val,n-1))
    return dp[n][TW]

val = [60, 100, 120]
wt = [10, 20, 30]
TW = 50
n = len(val)
dp = [[-1 for i in range(TW +1 )] for _ in range(n +1 )]
#print(dp)
print(knapsack(TW,wt,val,n))
