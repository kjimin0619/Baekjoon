from sys import stdin as s
n = int(s.readline())
nums = list(map(int,s.readline().split()))

for i in range(1,n):
    nums[i] = max(nums[i], nums[i-1]+nums[i])
print(max(nums))