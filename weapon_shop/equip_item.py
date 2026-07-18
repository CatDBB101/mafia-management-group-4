import data
# TODO: สร้างฟังก์ชัน equip_item(person, weapon)
#   - เช็คเงิน: เงินของ person ไม่พอราคา weapon -> ซื้อไม่ได้
#   - เช็คอาวุธ: person มีอาวุธอยู่แล้ว (equipment ไม่ใช่ "ไม่มี") -> ใส่เพิ่มไม่ได้
#   - ผ่านทั้งคู่ -> หักเงิน, เปลี่ยน equipment เป็นชื่ออาวุธ, บวก bonus เข้า power
#   - return {"status": True/False, "message": ข้อความบอกผล}
def get_money(person):
    for member in data.family_members:
        if member["name"] == person:
            return member['money']

def get_weapon(person):
    for member in data.family_members:
        if member["name"] == person:
            return member['equipment']

def get_weapon_price(nameweapon):
    for weapon_id, details in data.weapons_catalog.items():
        if details["name"] == nameweapon:
            return details["price"]

def Decrease_Money(person,price):
    for member in data.family_members:
        if member["name"] == person:
            member['money'] -= price


def equip_item(person,weapon):
    CanBuy = True
    MemberPoint = 0
    Moneyperson = get_money(person)
    Weaponperson = get_weapon(person)
    Weaponprice = get_weapon_price(weapon)
    if (Weaponperson != "ไม่มี"):
        CanBuy = False
        return "ใส่เพิ่มไม่ได้"
    if (Weaponprice > Moneyperson):
        CanBuy = False
        return "ซื้อไม่ได้"
    if (CanBuy):

        Decrease_Money(person,Weaponprice)
        for weapon_id, details in data.weapons_catalog.items():
            if details["name"] == weapon:
                Bonuspoint =  details["bonus"]
        for member in data.family_members:
            if member["name"] == person:
                    member['equipment'] = weapon
                    member['power'] += Bonuspoint
                    MemberPoint = member['power']
        print("Buy Success")
                    
    return True

    
