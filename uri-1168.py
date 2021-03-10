table = (6,2,5,5,4,5,6,3,7,6)
n = int(input())

for i in range(n):
    total=0
    nums=input()
    for j in nums:
        total=total+table[int(j)]
    print(total, 'leds')