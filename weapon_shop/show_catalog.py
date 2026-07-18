# =====================================================
#  weapon_shop/show_catalog.py — คนรับผิดชอบ: แบงค์
# =====================================================
from data import weapons_catalog

# TODO: สร้างฟังก์ชัน show_catalog()
#   - print อาวุธทุกชิ้นใน weapons_catalog บรรทัดละชิ้น (รหัส, ชื่อ, ราคา, พลังโบนัส)
def show_catalog():
 for num in weapons_catalog:
  
  weapons = weapons_catalog[num]
  print(f"{weapons["name"]},{weapons["bonus"]},{weapons["price"]}")

# ทดสอบ: python -m weapon_shop.show_catalog
if __name__ == "__main__":
 show_catalog()   # ต้องเห็นอาวุธครบ 3 ชิ้น




