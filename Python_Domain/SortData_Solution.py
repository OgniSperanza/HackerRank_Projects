rows, elements = map(int, raw_input().split())
row = []
for i in range(0, rows):
    row.append(map(int, raw_input().split()))
K = int(raw_input())
row = sorted(row, key=lambda a: a[K])
for i in range(0,rows):
    print str(row[i]).strip('[]').replace(',','')
