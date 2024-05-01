
laptops = int(input())

# price = list(map(int, input().split()))
# quality = list(map(int, input().split()))

laptopPrices = []
ans = "Poor Alex"

for i in range(laptops):
    p, q = map(int, input().split())
    
    laptopPrices.append([p, q])

laptopPrices.sort()

for i in range(laptops-1):
    if laptopPrices[i][1] > laptopPrices[i+1][1]:
        ans = "Happy Alex"
        break
    
print(ans)











# laptops = int(input())

# price = list(map(int, input().split()))
# quality = list(map(int, input().split()))

# alex = ""
# counts = 0

# for idx in range(laptops-1):
#     for elm in range(idx+1, laptops):
#         if price[idx] > price[elm]:
#             price[idx], price[elm] = price[elm], price[idx]
#             quality[idx], quality[elm] = quality[elm], quality[idx]
        
# for i in range(laptops-1):
#     print(counts)
#     if counts > 0:
#         break
    
#     for j in range(i+1, laptops):
#         if quality[i] > quality[j]:
#             counts += 1
#             print(counts)
#             break

# if counts == 0:
#     alex = "Poor Alex"
# else:
#     alex = "Happy Alex"
        
# print(alex)