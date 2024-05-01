def mergeSort(left, right, arr):
  if right == left:
    return [arr[left]]

  mid = left + (right-left)//2

  left_half = mergeSort(left, mid, arr)
  right_half = mergeSort(mid+1, right, arr)

  return merge(left_half, right_half)

def merge(lArr, rArr):
  l = 0
  r = 0
  ans = []

  while l < len(lArr) and r < len(rArr):
    if lArr[l] <= rArr[r]:
      ans.append(lArr[l])
      l += 1
    else:
      ans.append(rArr[r])
      r += 1

  while l < len(lArr) :
    ans.append(lArr[l])
    l += 1

  while r < len(rArr):
    ans.append(rArr[r])
    r += 1
  
  return ans
  
arr = [2, 3, 2, 5, 1, 3, -1]
ans = mergeSort(0, len(arr)-1, arr)
print(ans)