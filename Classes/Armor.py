import sys
from random import randint
from Classes.Item import Item
from Classes.Character import Character
from Classes.Weapon import Weapon


sys.stdout.reconfigure(encoding='utf-8')


'''
Ситуации для лука/оружия ближнего боя
'''
class Armor(Item):
    def __init__(self,
        name: str,  # Название предмета
        damage_reduction_percentage: int, #Процент снижения урона от атаки
        description: str = 'Защищает вас',  # Описание предмета
        use_text: str = 'Наносится удар по броне',
        rare: str = 'обычная', #редкость брони
    ):
        super().__init__(name, description, use_text, rare)
        self.damage_reduction_percentage = damage_reduction_percentage
    

    def print_info_about_item(self):
        super().print_info_about_item()

        print('Редкость брони:', self.rare)
        print('Снижение на', self.damage_reduction_percentage + '% урона от оружия')


    def use(self, What_beats: Weapon, who_beats: Character, target: Character, damage: int):
        super().use()

        procent_damage = (self.damage_reduction_percentage + randint(-2, 2))*self.dict_rare[self.rare]
        damage -= damage * (procent_damage/100) - target.armor_allowance
        who_beats.strike(target, damage, What_beats)
