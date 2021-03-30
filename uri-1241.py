while True:
    try: 
        test_case = int(input())
        for i in range (test_case):
            num1, num2 = map(int, input().split())

            if num1 < num2:
                print("nao encaixa")
            
            else:
                num1 = str(num1)
                num2 = str(num2)

                if num1[len(num1)-len(num2)::] == num2:
                    print("encaixa")
                else:
                    print("nao encaixa")
        
    except EOFError:
        break