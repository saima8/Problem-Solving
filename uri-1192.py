testCase = int(input())

for i in range (testCase):
    text = input()

    if (int(text[2])) == (int(text[0])):
        print((int(text[2])) * (int(text[0])))
    elif text[1].isupper():
        print((int(text[2])) - (int(text[0])))
    elif text[1].islower():
        print((int(text[2])) + (int(text[0])))