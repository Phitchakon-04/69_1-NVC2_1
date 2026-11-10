# ธัญชนก 

student_name = "ธัญชนก มังจันทึก"
print("==== โปรแกรมโดย: ", student_name, " ====")
product_list = []
i =1
print("n--- เริ่มกรอกขอมูลสินค้า (พิมพ์ "q" เพื่อหยุด) ---.")
while True:
    name_inqut = input(F"กรอกสินค้าชิ้นที่ {i}:")
    if name_input.lower() == "q":
        break
    price = float(input(f "กรอกราคาสินค้าชิ้นที่ {i}: "))
    vat_rate = float(input(f"กรอกอัตราภาษี vat (%) ชิ้นที่ {i}: "))
    vat_amount = price * (vat_rate / 100)
    total_price = price + vat_amount
    # bangkas
    product_list.append({
        "name": name_input,
        "price": price,
        "vat_rate": vat_rate,
        "vat_amount": vat_amount,
        "total_price": total_price
    })
    i += 1
    print("\n=== สรุปผลลัพธ์ภาษี vat และราคาสุทธิ ===")
    if len(product_list) > 0 :
        for  index, item in enumerate(product_list, start=1):
            print(f"ลำดับที่ { index} | สินค้า : {item[ "name"]} | ราคา: {item['price']} บาท {item['vat_amount']:.2f} รวม: {item['total_price']
            :.2f} บาท
            elsa:
            Print("ไม่มีการป้อนข้อมูลสินค้า")
            
    
