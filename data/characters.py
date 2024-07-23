import os, json

chara_path = 'data/json/'  # 人物json文件路径


class Characters:
    def __init__(self, chara):
        self.name = chara['name']
        self.attribute = chara['attribute']
        self.weapon_type = chara['weapon_type']
        self.attack = chara['attack']
        self.defense = chara['defense']
        self.health = chara['health']
        self.crit_rate = chara['crit_rate']['value']
        self.crit_damage = chara['crit_damage']['value']
        self.efficiency = chara['efficiency']['value']
        self.attack_rate = chara['attack_rate']['value']
        self.attribute_damage_enhancement = chara['attribute_damage_enhancement']['value']
        self.general_damage_enhancement = chara['general_damage_enhancement']['value']
        self.heavy_damage_enhancement = chara['heavy_damage_enhancement']['value']
        self.skill_damage_enhancement = chara['skill_damage_enhancement']['value']
        self.ending_damage_enhancement = chara['ending_damage_enhancement']['value']
        self.star = chara['star']
        self.sp = chara['sp']


class PiaoBoZheYanShe(Characters):
    """指定人物"""
    def __init__(self):
        global chara_path
        with open(chara_path + "PiaoBoZheYanShe.json", 'r', encoding='utf-8') as file:
            chara = json.load(file)
        super().__init__(chara)

    """计算函数"""
    def calculate(self):
        pass


class Jinhsi(Characters):
    """指定人物"""
    def __init__(self):
        global chara_path
        with open(chara_path + "Jinhsi.json", 'r', encoding='utf-8') as file:
            chara = json.load(file)
        super().__init__(chara)

    """计算函数"""
    def calculate(self, data):
        attack = data['attack'] * (1 + data['attack_rate']/100)
        result = attack
        return result


# 通过值寻找键
def find(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # 如果找不到匹配的值，返回None


"""通过字符串寻找类"""


def create_instance_by_name(class_name):
    cls = globals().get(class_name)
    if cls is not None and isinstance(cls, type):
        return cls()
    else:
        raise ValueError(f"Class {class_name} not found or is not a type.")


chara_dict = {}
for filename in os.listdir(chara_path):
    chara_dict[filename[:-5]] = create_instance_by_name(filename[:-5])