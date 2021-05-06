testCase = int(input())

for i in range (testCase):
    people = int(input())

    final = []

    for j in range (people):
        language = input()

        if language not in final:
            final.append(language)
    if len(final) > 1:
        print('ingles')
    else:
        print(final[0])
