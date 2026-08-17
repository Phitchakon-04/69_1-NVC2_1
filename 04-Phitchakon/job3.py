score = float(input("กรอกคะแนนของนักเรียน : "))


if score >= 80:
    print("เกรด A")
elif score >= 70:
    if score == 79 :
        print ("เกรด A ครูปัดให้")
    else:
        print("เกรด B")
elif score >= 60:
    print("เกรด C")
elif score >= 50:
    print("เกรด D")
else:
    print("เกรด F")