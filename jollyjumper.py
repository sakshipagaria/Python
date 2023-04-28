stack = []
n = int(input())
s = list(map(int, input().split()))
for i in range(1, n):
    stack.append(abs(s[i]-s[i-1]))
for i in range(1, n-1):
    if i != stack.pop():
        print("Not Jolly")
        break
else:
    print("jolly")
