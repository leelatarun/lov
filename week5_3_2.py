score = input("Enter Score: ")
sco = float(score)
if sco < 1.0 :
    if sco < 0.6 :
        print("F")
    elif sco >= 0.9 :
        print("A")
    elif sco >= 0.8 :
        print("B")
    elif sco >= 0.7 :
        print("c")
    else :
        print("D")
else :
    print("Enter under 1.0")
