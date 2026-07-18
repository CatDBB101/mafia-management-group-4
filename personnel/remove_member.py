# =====================================================
#  personnel/remove_member.py — คนรับผิดชอบ: peakza12
# =====================================================
from data import family_members

# TODO: สร้างฟังก์ชัน remove_member(target_name)
#   - หาคนที่ชื่อตรงกับ target_name (ไม่สนตัวพิมพ์ใหญ่/เล็ก) แล้วลบออกจาก family_members
#   - ลบสำเร็จ -> return True | ไม่เจอ -> return False
def remove_member(name):
    a = 0
    for i in family_members :
        if i["name"].lower() == name.lower():
            family_members.pop(a)
            return True
        a+= 1           
    return False


# ทดสอบ: python -m personnel.remove_member
if __name__ == "__main__":
    print(remove_member("luIgi"))   # ครั้งแรกต้องได้ True
    print(remove_member("Luigi"))   # ครั้งที่สองต้องได้ False (ลบไปแล้ว)
    print(family_members)           # ต้องเหลือแค่ Tony
