n, k = map(int, input().split())
arr = list(map(int, input().split()))

counts = 0

arr.sort()

ptr = k

while arr[ptr] < n-1 and arr[ptr] == arr[ptr+1]:
  ptr += 1

for idx in range(arr[ptr]):
  counts += 1
  
  if counts > k:
    counts = -1
    break

if counts < k:
  counts = -1
  
print(counts)