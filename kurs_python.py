s = input()

n = int(len(s) / 2) + 1

if s[:n] == s[-1 : -(n + 1) : -1]:
    print("YES")
else:
    print("NO")
