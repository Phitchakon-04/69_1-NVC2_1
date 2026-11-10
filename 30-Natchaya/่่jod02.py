# --- รับข้อมูลสินค้าชิ้นที่ 1 ---
name1 = input("กรอกชื่อสินค้าชิ้นที่ 1: ")
price1 = float(input("กรอกราคาต่อชิ้น: "))
quantity1 = int(input("กรอกจำนวนที่ขาย: "))
total1 = price1 * quantity1

# --- รับข้อมูลสินค้าชิ้นที่ 2 ---
name2 = input("กรอกชื่อสินค้าชิ้นที่ 2: ")
price2 = float(input("กรอกราคาต่อชิ้น: "))
quantity2 = int(input("กรอกจำนวนที่ขาย: "))
total2 = price2 * quantity2

# --- คำนวณยอดขายรวมทั้งหมด ---
grand_total = total1 + total2

# --- แสดงผลลัพธ์ ---
print("\n--- สรุปยอดขาย ---")
print("สินค้าที่ 1:", name1, "| ราคา:", price1, "บาท | จำนวน:", quantity1, "ชิ้น | รวม:", total1, "บาท")
print("สินค้าที่ 2:", name2, "| ราคา:", price2, "บาท | จำนวน:", quantity2, "ชิ้น | รวม:", total2, "บาท")
print("ยอดขายรวมทั้งหมด:", grand_total, "บาท")