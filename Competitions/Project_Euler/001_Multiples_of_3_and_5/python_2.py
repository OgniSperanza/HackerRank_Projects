nt = int(raw_input())
for i in range(0,nt):
    n = int(raw_input())-1
    x = (3 * (n//3) * ((n//3 +1)))//2
    y = (5 * (n//5) * ((n//5 +1)))//2
    z = (15 * (n//15) * ((n//15 +1)))//2
    ans = x + y - z
    print ans
