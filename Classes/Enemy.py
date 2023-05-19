import sys
from Classes.Character import Character


sys.stdout.reconfigure(encoding='utf-8')


class Enemy(Character):
    def __init__(
        self, 
        name: str, #Имя героя
        health: int, #Здоровье персонажа
        armor_used, #используемая броня
        weapon_used, #используемое оружие ближнего боя
        bow_used = None, #используемое оружие дальнего боя
        consumable_list: list = None, #список зелей, а нужен ли
        consumable_used = None, #используемые зелья, а нужны ли
        level: int = 1, #уровень персонажа
        artifact_list: list = list(), #различные предметы с баффами, а нужен ли
        artifact_used = None, #различные предметы с баффами
    ):
        super().__init__(name, health, level, list(), list(), consumable_list, list(), artifact_list)  
        self.armor_used = armor_used
        self.weapon_used = weapon_used
        self.bow_used = bow_used
        self.consumble_used = consumable_used
        self.artifact_used = artifact_used
    

    def print_info(self):#Мб подправить в будущем
        print('Поприветствуйте злодея ->', self.name)
        print('Уровень здоровья:', self.health)
        print('Уровень злодея:', self.level)