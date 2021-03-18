num=int(input())
for i in range(num):
    sentence = input()
    half = int(len(sentence)/2)
    firstHalf = sentence[:half]
    txt1 = firstHalf[::-1]
    secHalf = sentence[half:]
    txt2 = secHalf[::-1]
    print(f"{txt1}{txt2}")