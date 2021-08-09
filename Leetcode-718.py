# # def findLength(nums1, nums2):
# nums1 = [1,2,3,2,1]
# nums2 = [3,2,1,3,4]
        
# maxMatch = 0

# for i in range(len(nums1)):
#     for j in range(len(nums2)):
        
#         totalMatch = 0
        
#         i2 = i
#         j2 = j
        
#         while i2 < len(nums1) and j2 < len(nums2) and nums1[i2] == nums2[j2]:
#             totalMatch +=1
            
#             i2 += 1
#             j2 += 1
            
            
#         maxMatch = max (maxMatch, totalMatch)
        
# print (maxMatch)

# # Time complexity
# # nums1 length 1000, nums2 length 1000
# # total calculation 10^6
# # 3 operations -> n * m * (n * m)
# # calc becomes 10^9
# # O (n * m * (min(n,m)))
# # when n == m (worst case)
# # O(n * n * n) = O(n^3)
# # which gives time limit exceeded 

# matching = 0
# maxMatch(i, j):
# if i!= j:
#     matching = 0
# else:
#     matching = 1 + maxMatch(i+1, j+1)

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,3,4]

n = len(nums1)
m = len(nums2)

matching = [[0] * m for _ in range(n)] # Ref: The “_” is also a valid variable name in Python, people usually use it to indicate that the loop counter is not actually used in the loop....For example, it you want to create an array containing 5 zeros, you can simply write
# overall it's a n*m sized matrix
# [0 for _ in range(3)] == [0,0,0]

result = 0

for i in range (n-1, -1, -1):
    for j in range (m-1, -1, -1):
        if nums1[i] == nums2[j]:
            matching[i][j] = 1 + (matching[i+1][j+1] if i+1 < n and j+1 < m else 0)
            
            result = max(result, matching[i][j])
            
print (result)