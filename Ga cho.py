ga = 1
while ga <= 35:
    c = 1
    while c <= 35:
        if ga + c == 36:
            if 2 * ga + 4 * c == 100:
                print("Số gà =", ga)
                print("Số chó =", c)
                break
        c=c+1
    ga=ga+1
    
