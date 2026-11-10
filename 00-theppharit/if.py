price = float(input("ราคาห้องพัก : "))

if price >= 1200 :
    print("ห้องพรีเมียม")
elif price >= 800 :
    print("ห้องชั้นดี")
elif price >= 500 :
    print("ห้องธรรมดา")
else :
    print("เชิญไปที่อื่น")