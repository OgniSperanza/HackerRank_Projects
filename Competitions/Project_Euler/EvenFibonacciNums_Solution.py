t = int(raw_input())
for i in range(0, t):
    n = int(raw_input())
    x = [1,2]
    y = 0
    while (x[1] < n):
        if (x[1] % 2 == 0):
            y = y + x[1]
        tmp = x[1]
        x[1] = x[0] + x[1]
        x[0] = tmp
    print y  
