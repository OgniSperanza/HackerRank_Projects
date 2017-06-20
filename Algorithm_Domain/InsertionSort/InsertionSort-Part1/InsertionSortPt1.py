def insertionSort(ar):
    i = ar.__len__() -1
    e = ar[i]
    while i >= 1 and ar[i] >= e:
        if ar[i-1] > e:
            ar[i]= ar[i-1]
        elif ar[i -1] < e:
            ar[i]= e
        print str(ar).strip("[]").replace(",","")
        i = i -1
    if e < ar[0]:
        ar[0] = e
        print str(ar).strip("[]").replace(",","")
        
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
