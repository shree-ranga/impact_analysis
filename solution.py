"""
## Question

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

 

  Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773
"""
def solution(n):
    m = 4  # Fixed value of m
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(m):
        dp[0][i] = 1

    for i in range(1, n + 1):
        for j in range(m - 1, -1, -1):
            dp[i][j] = dp[i - 1][0] + dp[i - 1][j + 1]

    total_ways = dp[n][0]  # Total number of valid ways to attend classes
    ways_to_miss = dp[n - 1][1]  # Total number of ways to miss the last day

    return f"{ways_to_miss}/{total_ways}"  # Return the probability of missing the graduation ceremony

print(solution(5))  # Output: 14/29
print(solution(10))  # Output: 372/773