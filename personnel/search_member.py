# =====================================================
#  personnel/search_member.py — คนรับผิดชอบ: ราชาแอ็กเกอร์ตัวปลอม
# =====================================================
from data import family_members

# TODO: สร้างฟังก์ชัน search_member(target_name)
#   - หาคนใน family_members ที่ชื่อตรงกับ target_name (ไม่สนตัวพิมพ์ใหญ่/เล็ก)
#   - เจอ -> return dict ของคนนั้น | ไม่เจอ -> return None

def search_member (name) :
    result = None
    for member in family_members:
        if member["name"].lower() == name.lower():
            result = member
        else : 
            result == "ไม่พบสมาชิค"
    return result
            
if __name__ == "__main__":
    print(search_member("tony"))


# ต้องได้ dict ของ Tony (พิมพ์เล็กก็ต้องเจอ)
# ทดสอบ: python -m personnel.search_member
# ต้องได้ None
