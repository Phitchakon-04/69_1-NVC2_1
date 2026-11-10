def Products(name, price):
    # คำนวณ ปราย
    vat = price * 0.07
    # คำนวณ พิมพ์ลภัส
    tatal_price = price + vat
    
    print(f"- - -รายละเอียดสินค้า: {name} ---")
    print(f"ราคาสินค้า: {price:.2f} บาท")
    print(f"ภาษี vat 7%: {vat:.2f} บาท")
    print(f"ภาษีรวมภาษี (สุทธิ): {tatal_price:.2f} บาท\n")

# รับข้อมูล ปราย
for i in range(1, 6):
    print(f"กรุณากรอกข้อมูลสินค้าชิ้นที่ {i}")
    product_name = input("ชื่อสินค้า: ")
    product_price = float(input("ราคาสินค้า: "))

    # เรียกใช้ พิมพ์ลภัส
    Products(product_name, product_price)