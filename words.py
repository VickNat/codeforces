# size = int(input())
# distinctWords = []
# wordsCount = []

# for words in range(size):
#     temp = input()

#     if temp in distinctWords:
#         wordsCount[distinctWords.index(temp)]+=1
#     elif temp not in distinctWords:
#         distinctWords.append(temp)
#         wordsCount.append(1)

# print(len(distinctWords))
# print(*wordsCount)


# n = int(input())
# counts = {}

# for idx in range(n):
#     word = input()
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1

# print(len(counts))

# for idx in counts:
#     print(counts[idx], end=" ")

# T = int(input())
#
# for inputs in range(T):
#     n = int(input())
#     blocks = list(map(int, input().split()))
#
#     left = 0
#     right = n - 1
#     prev = max(blocks)
#     answer = "Yes"
#
#     while (right >= left):
#         if blocks[right] >= blocks[left]:
#             hold = blocks[right]
#             right -= 1
#         else:
#             hold = blocks[left]
#             left += 1
#
#         if prev >= hold:
#             prev = hold
#         else:
#             answer = "No"
#             break
#
#     print(answer)

'''temp = ""
    for i in s:
        if i.isupper():
            temp+=i.lower()
        else:
            temp += i.upper()
    return temp'''

'''
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        else:
            otherHalf = 0
            
            while x > otherHalf:
                otherHalf = (otherHalf*10) + x%10
                x//=10
                    
            if otherHalf == x or x == otherHalf//10:
                return True
            else:
                return False
'''
'''
        if len(strs) == 0:
            return ""
        
        pref_str = strs[0]
        
        for str_idx in strs:
            for index in range(0, len(pref_str)):
                if index >= len(str_idx) or pref_str[index] != str_idx[index]:
                    pref_str = pref_str[0:index]
                    break
                    
        return pref_str
'''