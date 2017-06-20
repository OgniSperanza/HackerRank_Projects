T = int(raw_input())
for _ in range(0, T):
    N = int(raw_input())
    nums = map(int, raw_input().split())
    ans = False
    left = 0
    right = sum(nums[1::])
    for i in range(1, N):
        left = left + nums[i-1]
        right = right - nums[i]
        if left == right:
            ans = True
    if ans or nums.__len__() == 1:
        print "YES"
    else:
        print "NO"
