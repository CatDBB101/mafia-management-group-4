# =====================================================
#  missions/send_mission.py — คนรับผิดชอบ: ______________________
# =====================================================
from data import family_members
from personnel.remove_member import remove_member
list_mission = {
    "1": {"mission_name": "ปราบสัตว์ประหลาด", "power_need": 7, "reward": 20000},
    "2": {"mission_name": "หาตัวประธาน", "power_need": 3, "reward": 50000},
    "3": {"mission_name": "ยิงปืนใส่งู", "power_need": 2, "reward": 10000}
}

# TODO: (OPTIONAL) สร้างฟังก์ชัน send_mission(person)
#   - power ของ person >= 7 -> บวกเงินรางวัล 300000 เข้าเงินของ person
#     แล้ว return {"status": True, "reward": 300000}
#   - ไม่ถึงเกณฑ์ -> return {"status": False, "reward": 0}
#   (การลบคนที่ตาย main.py จัดการเอง)
def get_power(person):
    for member in family_members:
        if member["name"] == person:
            return member['power']
    return False

def add_Money(person,price):
    for member in family_members:
        if member["name"] == person:
            member['money'] += price
            print(f"สำเร็จ และ บวกเงินรางวัล",member['money'],"เพิ่มเข้าไปในกระเป๋าของลูกน้องคนนั้น")

def show_mission():
    for num in list_mission:
        listt = list_mission[num]
        print(f"{num},'Mission Name : ',{listt['mission_name']},'Power Need :',{listt['power_need']},'Reward : ',{listt['reward']}")
    choose_choice = input("Choose 1 - 3 : ")
    for num in list_mission:
         if (choose_choice == num):
              return choose_choice
         
def send_mission():
        person = input("จะส่งใครไปตาย : ")
        Choose_Mission = show_mission()
        power = get_power(person)
        if (power == False):
             return "ไม่มีชื่อคนนี้ในระบบ"
        else:
            for num in list_mission:
                powermission = list_mission[num]
                if (Choose_Mission == num):
                    if (power < powermission['power_need']):
                                result = remove_member(person)
                                if (result):
                                    print(f"กำจัด {person} เรียบร้อยออกจากแฟมิลี่เรียบร้อย")
                                else:
                                    print(f"ไม่เจอสมาชิกชื่อ {person}")
                                    return {"status": False, "reward": 0}
                    elif (power >= powermission['power_need']):
                        add_Money(person,powermission['reward'])
                        return {"status": True, "reward": powermission['reward']}
        

# ทดสอบ: python3 -m missions.send_mission
# if __name__ == "__main__":
#      print(send_mission("fsafasf"))

