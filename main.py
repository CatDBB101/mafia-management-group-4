# =====================================================
#  main.py — ศูนย์กลางของระบบ (งานของหัวหน้ากลุ่ม!)
#
#  เมนู 1-6 หัวหน้าเขียนเอง โดยเรียกใช้ฟังก์ชันที่เพื่อนเขียน
#  pattern เดียวกันทุกเมนู:  รับ input -> เรียกฟังก์ชัน -> print ผลลัพธ์
#
#  สำคัญ: ไฟล์นี้จะรันได้ก็ต่อเมื่อทุกไฟล์ประกาศฟังก์ชันแล้ว
#  -> งานแรกของทุกคน: สร้างโครงฟังก์ชันตัวเอง (def ... + pass) แล้ว push ทันที
# =====================================================
from data import weapons_catalog
from personnel.add_member import add_member
from personnel.show_members import show_members
from personnel.search_member import search_member
from personnel.remove_member import remove_member
from weapon_shop.show_catalog import show_catalog
from weapon_shop.equip_item import equip_item
# from missions.send_mission import send_mission

def main():
    while True:
        print("\n=== MAFIA MANAGEMENT SYSTEM ===")
        print("1. รับลูกน้องใหม่")
        print("2. ดูรายชื่อแก๊ง")
        print("3. ค้นหาประวัติ")
        print("4. สั่งเก็บลูกน้อง")
        print("5. คลังอาวุธ")
        print("6. ส่งไปทำภารกิจ")
        print("7. ออกจากระบบ")

        choice = input("เลือกคำสั่ง (1-7): ")

        # ---------- เมนู 1 ----------
        if choice == '1':
            print("\n--- เพิ่มลูกน้องใหม่ ---")
            name = input("name :")
            age = int(input("age :"))
            power = int(input("power :"))
            money = float(input("money :"))

            add_member(name, age, power, money)
            # TODO: รับ name, age, power, money (age/power ใช้ int(), money ใช้ float())
            #       -> add_member(...) -> print เพิ่ม (ชื่อ) ในตำแหน่ง (role) เรียบร้อยแล้ว
            print("เพิ่มสมาชิกใหม่เรียบร้อย")

        # ---------- เมนู 2 ----------
        elif choice == '2':
            print("\n--- รายชื่อลูกน้องทั้งหมด ---")
            show_members()
            # TODO: เรียก show_members()

        # ---------- เมนู 3 ----------
        elif choice == '3':
            print("\n--- ค้นหาประวัติ ---")
            name = input("name :")
            target_data = search_member(name)
            if target_data == None:
                print("ไม่เจอข้อมูลสมาชิก")
            else:
                print(target_data)
            # TODO: รับชื่อ -> search_member() -> เจอ: print ข้อมูล | ไม่เจอ: print ไม่พบชื่อในระบบ

        # ---------- เมนู 4 ----------
        elif choice == '4':
            name = input("name :")
            result = remove_member(name)
            if (result):
                print(f"กำจัด {name} เรียบร้อย")
            else:
                print(f"ไม่เจอสมาชิกชื่อ {name}")

        # ---------- เมนู 5 ----------
        elif choice == '5':
            show_catalog()

        # ---------- เมนู 6 (OPTIONAL) ----------
        elif choice == '6':
            print("\n--- ส่งไปทำภารกิจ ---")
            # TODO: รับชื่อ -> search_member() -> send_mission()
            #       -> สำเร็จ: print เงินรางวัล + ยอดเงินปัจจุบัน | ล้มเหลว: remove_member() + print ถูกลบ
            print("!! เมนูนี้ยังไม่ถูกเชื่อม")

        elif choice == '7':
            print("ปิดระบบ...")
            break

        else:
            print("คำสั่งไม่ถูกต้อง")

if __name__ == "__main__":
    main()
