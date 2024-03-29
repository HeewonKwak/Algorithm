# 2 x n 타일링
# https://school.programmers.co.kr/learn/courses/30/lessons/12900
def solution(n):
    answer = 0
    dp = [0] * (n + 2)
    dp[1] = 1
    dp[2] = 1
    for i in range(1, n):
        dp[i+2] = dp[i+1] % 1000000007 + dp[i]
    return dp[n+1] % 1000000007

# 복습
def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n]