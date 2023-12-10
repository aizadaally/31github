# Contest 1
# x = int(input())
# y = list(map(int, input().split()))
# dp[4005][4005] = n,k, used[4005][4005]
# for i in range(0,y):
#     if i+1:
#         print(dp[i-y[i]])
#         if i+2:
#             print(dp[3*y[i]])
#2

# n = int(input())
# h = list(map(int, input().split()))
# for i in range(1,h+1):
#     dp = list([0] for i in range(0, n+1)):
#     dp[1] = 0
#     dp[2] = abs(h[2] - h[1])
#     a = int(input())
#     a = dp[i - 1] + abs(h[i] - h[i - 1])
#                     b = int(input())
#                         b = dp[i - 2] + abs(h[i] - h[i - 2])
#                         for i in range (1, i+1):
#                             dp[i] = min(a, b);
# 1                            print(dp[i])
# m = int(input())
# l = [0] + list(map(int, input().split()))
# dp = {}
# dp[1] = 0
# dp[2] = abs(l[1] - l[2])
#
# for i in range(3, m+1):
#     dp[i] = min(dp[i-1] + abs(l[i] - l[i-1]), dp[i-2] + abs(l[i] - l[i-2]))
#
# print(dp[m])

 # 1


    # import java.util. *;
        #
        # class Main
        #
        #
        # {
        #
        #     static
        # int
        # h[], dp[];
        #
        # public
        # static
        # void
        # main(String[]
        # args)
        #
        # {
        #
        #     Scanner
        # con = new
        # Scanner(System. in);
        #
        # int
        # n = con.nextInt();
        #
        # h = new
        # int[n + 1];
        #
        # dp = new
        # int[n + 1];
        #
        # for (int i = 1; i <= n; i++)
        #
        # h[i] = con.nextInt();
        #
        #
        #



        #
        # {
        #


        #
        # }
        #
        #
        #
        # System.out.println(dp[n]);
        #
        # con.close();
        #
        # }
        #
        # }

# from sys import stdin, stdout
# m = int(stdin.readline())
# b =[0] + list(map(int, stdin.readline().split()))
# dp = [0]*int(1e6 +5)
# dp[1] = 0
# dp[2] =abs(a[2]-a[1])
# for i in range(3, n+1):
#     dp[i]=min(abs(i-1)-a[i])+dp[i-1],3*abs(a[i-2]-a[i])+dp[i-2])
# Dice Combination
# n = [0]+list(map(int, input().split()))
# dp = [0]*int(10**9+7)
# dp [0]=1
# x= int(input())
# for i in n:
#     for x in (1, x+1):
#         if i-x>=0:
#             dp[i] = (dp[i]+dp[i-x])
# dp%(10**9+7)
# print(dp(n))

# Minimizing costs
# n = int(input())
# m = list(map(int,input().split()))
# x= int(input())
# q = list(map(int, input().split()))
# dp = [0]*int(10**6)
# dp[0] =1
# for i in range in n:
#     for

# Bookshop
# n = int(input())
# m = tuple(map(int, input().split()))
# x = list(map(int, input().split()))
# dp = {}
# for i in range(n):
#     s = int(input())
# print(len(s))

#4 10
#4 8 5 3
#5 12 8 1
  #1 Platforms
# n = int(input())
# m = list(map(int, input().split()))
# dp = {}
# dp[1] = 0
# for i in m:
#     dp[i]= abs(y[i]-y[i-1])
#     dp[2]= abs([i+1]-[i])
#     print(min(dp[2], [i]))

# n = int(input())
# m = list(map(int, input().split()))
# a = int(input())
# b = int(input())
# dp[102] = {102}

n, s = map(int, input().split())
a = [[] for _ in range(105)]
result = 0
visited = [False] * 105

for i in range(1, n + 1):
    for j in range(1, n + 1):
        row = list(map(int, input().split()))
        for k in row:
            if k == 1:
                a[i].append(j)

print(a)

def dfs(v):
    global result, visited, a
    result += 1
    visited[v] = True
    for i in range(n + 1):
        to = a[v][i]
        if not visited[to]:
            dfs(to)

dfs(s)
print(result)
# n, s = map(int, input().split())
# a = [[] for _ in range(105)]
# result = 0
# visited = [False] * 105
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         row = list(map(int, input().split()))
#         for k in row:
#             if k == 1:
#                 a[i].append(j)
#
# print(a)
#
# def dfs(v):
#     global result, visited, a
#     result += 1
#     visited[v] = True
#     for i in range(n + 1):
#         to = a[v][i]
#         if not visited[to]:
#             dfs(to)
#
# dfs(s)
# print(result)


# n, v = map(int, input().split())
# m = []
# for _ in range(n):
#     m.append([0] + list(map(int, input().split())))
# used = [False] * (n+1)
# ans = 0
#
#
# def dfs(s):
#     global ans
#     used[s] = True
#     ans += 1
#     for i in range(1, n+1):
#         if (m[s][i] == 1) and (used[i] is False):
#             dfs(i)

#
# dfs(v)
# print(ans)


from sys import stdin, stdout

result = 0
n, s = map(int, stdin.readline().split())

a = [[] for _ in range(105)]

visited = [False] * 105

for i in range(1, n + 1):
    row = list(map(int, stdin.readline().split()))
    for j in range(1, n + 1):
        if row[j - 1] == 1:
            a[i].append(j)


def dfs(v):
    global result, visited, a
    visited[v] = True
    result += 1
    for i in a[v]:
        if not visited[i]:
            dfs(i)


dfs(s)
stdout.write(str(result))