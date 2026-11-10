# รับราคาสินค้าและอัตราภาษี VAT จากผู้ใช้
price = float(input("ป้อนราคาสินค้า: "))
vat_rate = float(input("ป้อนอัตราภาษี VAT (เป็นเปอร์เซ็นต์ เช่น 7): "))

# คำนวณภาษี VAT และราคารวมสุทธิ (ราคารวมภาษี VAT)
vat_amount = price * (vat_rate / 100)
total_price = price + vat_amount

# แสดงผลลัพธ์ออกทางหน้าจอ
print("-" * 30)
print(f"ราคาสินค้าตั้งต้น: {price:.2f} บาท")
print(f"มูลค่าภาษี VAT ({vat_rate}%): {vat_amount:.2f} บาท")
print(f"ราคารวมสุทธิ (ราคารวมภาษี): {total_price:.2f} บาท")
print("-" * 30)