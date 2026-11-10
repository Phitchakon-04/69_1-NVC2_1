
# โปรแกรมคำนวณภาษีมูลค่าเพิ่ม VAT[span_1](start_span)[span_1](end_span)

vat_rate = float(input("กรุณาป้อนอัตราภาษี VAT (%): "))

def Products(name, price):
    vat = price * vat_rate / 100
    total = price + vat

    print("\nชื่อสินค้า:", name)
    print("ราคาสินค้า:", price, "บาท")
    print("ภาษี VAT:", vat, "บาท")
    print("ราคารวมภาษี:", total, "บาท")

# รับข้อมูลสินค้า 5 ชิ้น[span_10](start_span)[span_10](end_span)
for i in range(5):
    print("\nสินค้า", i + 1)
    name = input("กรุณาป้อนชื่อสินค้า: ")
    price = float(input("กรุณาป้อนราคาสินค้า: "))

    Products(name, price)