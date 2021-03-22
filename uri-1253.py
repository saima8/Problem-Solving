num = int(input())

for i in range(num):
    text = input()
    num = int(input())
    t_new = ''
    for l in text:
        position = ord(l)-num

        if(position < 65):
            t_new += chr(91-(65-position))
        else:
            t_new += chr(ord(l)-num)
    print(t_new)