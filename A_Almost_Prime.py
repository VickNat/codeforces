'''
list(map(int, input().split()))
int(input())
'''

def isPrime(num):
  d = 2
  prime = set()

  while d*d <= num:
    while num%d == 0:
      prime.add(d)
      num //= d
    
    d += 1
  
  if num > 1:
    prime.add(num)
  
  return len(prime) == 2

def main():
  num = int(input())
  counts = 0

  for elm in range(6, num+1):
    if isPrime(elm):
      counts += 1
  
  print(counts)

main()
