numbers=[]

test_case = int(input())
for j in range (test_case):
    num = int(input())
    numbers.append(num)

numbers.sort()

finalList = []
for k in numbers:
    if k not in finalList:
        finalList.append(k)

for i in (finalList):
    counter_num = numbers.count(i) 
    print(f"{i} aparece {counter_num} vez(es)")