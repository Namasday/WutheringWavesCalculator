chara_dict_data = {
    'PiaoBoZheYanShe':
        {
            'name': "漂泊者",
            'attribute': "衍射",
            'weapon_type': "迅刀",
            'attack': 375,
            'defense': 1368,
            'health': 11400,
            'crit_rate': 20,        # 鸣链1：技能后加暴击率15%
            'crit_damage': 150,     #
            'efficiency': 120,
            'attack_rate': 27,      # 技能边路加攻12%，技能中路2：重击鸣奏后加攻15%
            'attribute_damage_enhancement': 32,     # 技能边路增伤12%
            'general_damage_enhancement': 0,
            'heavy_damage_enhancement': 0,
            'skill_damage_enhancement': 60,     # 技能中路1增伤60%
            'ending_damage_enhancement': 40,
            'sp': "重击鸣奏加攻15%（已计入），技能加暴15%（已计入）,技能或大招使目标降低10%抗性"
        },
    'WeiLiNai':
        {
            'name': "维里奈",
            'attribute': "衍射",
            'weapon_type': "音感仪",
            'attack': 337,
            'defense': 1099,
            'health': 14237,
            'crit_rate': 5,
            'crit_damage': 150,
            'efficiency': 100,
            'attack_rate': 32,      # 技能边路加攻12%，技能中路1：重击、空中攻击、大招后加攻20%
            'attribute_damage_enhancement': 15,     # 鸣链4：重击、空中攻击、大招后增伤15%
            'general_damage_enhancement': 20,       # 鸣链6：空中攻击增伤20%
            'heavy_damage_enhancement': 20,     # 鸣链6：重击增伤20%
            'skill_damage_enhancement': 0,
            'ending_damage_enhancement': 0,
            'sp': "鸣链6只增伤重击和空中攻击（已计入）"
        },
    'AnKe':
        {
            'name': "安可",
            'attribute': "热熔",
            'weapon_type': "音感仪",
            'attack': 425,
            'defense': 1246,
            'health': 10512,
            'crit_rate': 5,
            'crit_damage': 150,
            'efficiency': 100,
            'attack_rate': 37,       # 技能边路加攻12%，鸣链6：大招期间普攻加攻25%
            'attribute_damage_enhancement': 64,      # 技能边路增伤12%，技能中路1：生命高于70%增伤10%，技能中路2：技能后增伤10%，鸣链1：12%，鸣链4：重击增伤20%
            'general_damage_enhancement': 0,
            'heavy_damage_enhancement': 0,
            'skill_damage_enhancement': 0,
            'ending_damage_enhancement': 0,
            'sp': ""
        },
    'PiaoBoZheYanMie':
        {
            'name': "漂泊者",
            'attribute': "衍射",
            'weapon_type': "迅刀",
            'attack': 375,
            'defense': 1368,
            'health': 11400,
            'crit_rate': 5,
            'crit_damage': 150,
            'efficiency': 100,
            'attack_rate': 0,
            'attribute_damage_enhancement': 0,
            'general_damage_enhancement': 0,
            'heavy_damage_enhancement': 0,
            'skill_damage_enhancement': 0,
            'ending_damage_enhancement': 0,
            'sp': "重击加攻15%（已计入），技能加暴15%（已计入）,技能或大招使目标降低10%抗性"
        },
    'LingYang':
        {
            'name': "漂泊者",
            'attribute': "衍射",
            'weapon_type': "迅刀",
            'attack': 375,
            'defense': 1368,
            'health': 11400,
            'crit_rate': 5,
            'crit_damage': 150,
            'efficiency': 100,
            'attack_rate': 0,
            'attribute_damage_enhancement': 0,
            'general_damage_enhancement': 0,
            'heavy_damage_enhancement': 0,
            'skill_damage_enhancement': 0,
            'ending_damage_enhancement': 0,
            'sp': "重击加攻15%（已计入），技能加暴15%（已计入）,技能或大招使目标降低10%抗性"
        },
    'KaKaLuo':
        {
            'name': "漂泊者",
            'attribute': "衍射",
            'weapon_type': "迅刀",
            'attack': 375,
            'defense': 1368,
            'health': 11400,
            'crit_rate': 5,
            'crit_damage': 150,
            'efficiency': 100,
            'attack_rate': 0,
            'attribute_damage_enhancement': 0,
            'general_damage_enhancement': 0,
            'heavy_damage_enhancement': 0,
            'skill_damage_enhancement': 0,
            'ending_damage_enhancement': 0,
            'sp': "重击加攻15%（已计入），技能加暴15%（已计入）,技能或大招使目标降低10%抗性"
        },
    'JianXin':
        {
            'name': "漂泊者",
            'attribute': "衍射",
            'weapon_type': "迅刀",
            'attack': 375,
            'defense': 1368,
            'health': 11400,
            'crit_rate': 5,
            'crit_damage': 150,
            'efficiency': 100,
            'attack_rate': 0,
            'attribute_damage_enhancement': 0,
            'general_damage_enhancement': 0,
            'heavy_damage_enhancement': 0,
            'skill_damage_enhancement': 0,
            'ending_damage_enhancement': 0,
            'sp': "重击加攻15%（已计入），技能加暴15%（已计入）,技能或大招使目标降低10%抗性"
        },
    'JiYan':
        {
            'name': "漂泊者",
            'attribute': "衍射",
            'weapon_type': "迅刀",
            'attack': 375,
            'defense': 1368,
            'health': 11400,
            'crit_rate': 5,
            'crit_damage': 150,
            'efficiency': 100,
            'attack_rate': 0,
            'attribute_damage_enhancement': 0,
            'general_damage_enhancement': 0,
            'heavy_damage_enhancement': 0,
            'skill_damage_enhancement': 0,
            'ending_damage_enhancement': 0,
            'sp': "重击加攻15%（已计入），技能加暴15%（已计入）,技能或大招使目标降低10%抗性"
        },
}

weapon_stars: int = 1
weapon_dict_data = {
    'YiLanFuLu':
        {
            'name': "漪澜浮录",
            'type': "音感仪",
            'attack': 500,
            'attack_rate': 53.9,
            'general_damage_enhancement': (2.4+0.8*weapon_stars)*5,
            'sp': ""
        },
    'CheKuiZhiShou':
        {
            'name': "掣傀之手",
            'type': "音感仪",
            'attack': 500,
            'crit_rate': 36,
            'attribute_damage_enhancement': 9+3*weapon_stars,
            'attack_rate': (9+3*weapon_stars)*2,
            'sp': "自身不在场时，该效果攻击额外提升9+"+str(3*weapon_stars)+"%",
        }
}