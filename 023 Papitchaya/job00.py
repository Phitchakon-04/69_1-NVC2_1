# รับราคาสินค้าและอัตราภาษี VAT จากผู้ใช้[span_1](start_span)[span_1](end_span)
price = float(input("ป้อนราคาสินค้า: "))
vat_rate = float(input("ป้อนอัตราภาษี VAT (เป็นเปอร์เซ็นต์ เช่น 7): "))

# คำนวณภาษี VAT และราคารวมสุทธิ (ราคารวมภาษี VAT)[span_2](start_span)[span_2](end_span)
vat_amount = price * (vat_rate / 100)
total_price = price + vat_amount

# แสดงผลลัพธ์ออกทางหน้าจอ[span_3](start_span)[span_3](end_span)
print("-" * 30)
print(f"ราคาสินค้าตั้งต้น: {price:.2f} บาท")
print(f"มูลค่าภาษี VAT ({vat_rate}%): {vat_amount:.2f} บาท")
print(f"ราคารวมสุทธิ (ราคารวมภาษี): {total_price:.2f} บาท")
print("-" * 30)