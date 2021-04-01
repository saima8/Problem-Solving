test_case = int(input())

for i in range (test_case):
    text = input().lower()
    letters = {}
    for c in text:
        if c.isalpha() and c not in letters:
            letters[c] = text.count(c)

    sorted_letters = sorted(letters.items(), key= lambda x: (-x[1], x[0])) 
    main = sorted_letters[0][1]
    result = ''
    for c in sorted_letters:
        if c[1] == main:
            result += c[0]
        else:
            break
    print(result)