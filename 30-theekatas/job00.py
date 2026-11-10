price = float(input("กรอกราคาสินค้า: "))
vat = float(input("กรอกอัตราภาษี VAT (%): "))

vat_amount = price * (vat / 100)
total_price = price + vat_amount

print("ภาษี VAT =", vat_amount,"บาท")
print("ราคาสุทธิ =", total_price,"บาท")