goal = 200

streak = 0

for8 = streak%8
geekbits = 0
days = 0

for i in range(goal+1):
    days +=1
    for8 += 1
    geekbits +=1

    # print(days, for8, geekbits)

    if for8 == 8:
        geekbits +=8
        for8 = 0

    if geekbits >= goal:
        print(days)
        break
    
    # 1.1.1 2.2.2 3.3.3 4.4.4 5.5.5 6.6.6 7.7.7 8.0.16