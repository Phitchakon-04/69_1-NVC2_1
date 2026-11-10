students = [
    ("ชลรดา", "ชุมจันทร์", 17, "081-234-5678"),
    ("วรฤทัย", "องอาจ", 17, "089-876-5432"),  
]
print("--- ข้อมูลนักเรียนห้อง ปวช.2 ทด1 ---")

for index, student in enumerate(students, start=1):
  name, surname, age, phone = student
  print(
      f"คนที่ {index}: ชื่อ-นามสกุล: {name} {surname} | อายุ: {age} ปี |"
      f" เบอร์โทร: {phone}"
  )

print("\n--- รายชื่อเพื่อนสนิท 2 คน ---")
best_friend_1 = students[0][0]  
best_friend_2 = students[1][0]  

print(f"1. {best_friend_1}")
print(f"2. {best_friend_2}")