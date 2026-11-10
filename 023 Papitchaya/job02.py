# โปรแกรมคำนวณภาษีมูลค่าเพิ่ม VAT

vat_rate = float(input("กรุณาป้อนอัตราภาษี VAT (%): "))


def Products(name, price, vat_rate):
    vat_amount = price * (vat_rate / 100)
    total_price = price + vat_amount
    
    print("--- ผลลัพธ์: {} ---".format(name))
    print("ราคาสินค้า: {:,.2f} บาท".format(price))
    print("ภาษี VAT ({}%): {:,.2f} บาท".format(vat_rate, vat_amount))
    print("ราคาสุทธิ: {:,.2f} บาท\n".format(total_price))


vat_input = float(input("กรุณาป้อนอัตราภาษี VAT (%): "))
print("=" * 40)

for i in range(1, 6):
    print("กรุณาป้อนข้อมูลสินค้าชิ้นที่ {}".format(i))
    product_name = input("ชื่อสินค้าชิ้นที่ {}: ".format(i))
    product_price = float(input("ราคาสินค้าชิ้นที่ {} (บาท): ".format(i)))
    
    Products(product_name, product_price, vat_input)