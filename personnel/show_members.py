# =====================================================
#  personnel/show_members.py — คนรับผิดชอบ: ______________________
# =====================================================
from data import family_members

# TODO: สร้างฟังก์ชัน show_members()
#   - print ข้อมูลลูกน้องทุกคนใน family_members บรรทัดละคน (ชื่อ, ตำแหน่ง, ความโหด, อาวุธ)
def show_members():
    print("Member List")
    print("=" * 50)
    for member in family_members:
        print(f"{member['name']}({member['role']}) - power:{member['power']} money:{member['money']} equipment:{member['equipment']}")
    print("=" * 50)

# ทดสอบ: python -m personnel.show_members
if __name__ == "__main__":
    show_members()   # ต้องเห็น Tony กับ Luigi คนละบรรทัด
