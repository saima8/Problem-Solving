# def findLength(nums1, nums2):
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,3,4]
        
maxMatch = 0

for i in range(len(nums1)):
    for j in range(len(nums2)):
        
        totalMatch = 0
        
        i2 = i
        j2 = j
        
        while i2 < len(nums1) and j2 < len(nums2) and nums1[i2] == nums2[j2]:
            totalMatch +=1
            
            i2 += 1
            j2 += 1
            
            
        maxMatch = max (maxMatch, totalMatch)
        
print (maxMatch)