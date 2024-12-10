Score = int(input("What did you score: "))

if Score >= 70:
    print("A Grade")
elif 60 <= Score < 70:
    print("B Grade")
elif 50 <= Score < 60:
    print("C Grade")
elif 40 <= Score < 50:
    print("D Grade")
else:
    print("You failed")