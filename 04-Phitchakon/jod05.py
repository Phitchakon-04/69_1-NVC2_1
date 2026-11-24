def info(**Peach):
    print("สวัสดี คุณ" ,Peach["name"])
    print("ยินดีต้อนรับสู่ห้องเรียน" ,Peach["room"])
    print("อายุ" ,Peach["age"])
    print("สีที่ชอบ" ,Peach["color"])
    print("จังหวัด" ,Peach["province"])

info(
    name = "พีช" ,
    room = "อาชีวะ" ,
    age = 17 ,
    color = "ชมพูพาสเทล" ,
    province = "นครราชสีมา"
)