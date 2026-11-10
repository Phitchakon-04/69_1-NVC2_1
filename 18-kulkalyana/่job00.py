student_name = "กุลกัลยาณ์ หวังคละกลาง"
print("=== โปรแกรมโดย:", student_name, "===")

product_list = []
i = 1

print("\n--- เริ่มกรอกข้อมูลสินค้า (พิมพ์ 'q' เพื่อหยุด) ---")
while True:
    name_input = input(f"กรอกชื่อสินค้าชิ้นที่ {i}: ")
    if name_input.lower() == 'q':
        break
        
    price = float(input(f"กรอกราคาสินค้าชิ้นที่ {i}: "))
    vat_rate = float(input(f"กรอกอัตราภาษี VAT (%) ชิ้นที่ {i}: "))
    
    vat_amount = price * (vat_rate / 100)
    total_price = price + vat_amount
    
    product_list.append({
        "name": name_input,
        "price": price,
        "vat": vat_amount,
        "total": total_price
    })
    
    i = i + 1

print("\n=== สรุปผลลัพธ์ภาษี VAT และราคาสุทธิ ===")
if len(product_list) > 0:
    for index, item in enumerate(product_list, start=1):
        print(f"ลำดับที่ {index} | สินค้า: {item['name']} | ราคา: {item['price']} บาท | VAT: {item['vat']:.2f} บาท | ราคารวมสุทธิ: {item['total']:.2f} บาท")
else:
    print("ยังไม่มีการป้อนข้อมูลสินค้า")