import sys
from random import randint, random
from Classes.Character import Character
from Classes.Item import Item


sys.stdout.reconfigure(encoding='utf-8')


class Weapon(Item):
    def __init__(
        self,
        name: str,  # Название предмета
        damage: int,  # Урон
        crit_damage: int,  # Критический урон
        crit_chance: float,  # Шанс крита: от 0 и до 1. 0.5 = 50%, 0.2 = 20% и т.д.
        places_to_hit_and_their_chance: dict = {
            'голова': lambda: randint(1, 5),
            'туловище': lambda: randint(1, 2),
            'руки': lambda: randint(1, 3),
            'ноги': lambda: randint(1, 3)
        },
        description: str = 'Это меч или лук или посох',  # Описание предмета
        use_text: str = '{0} целится, используя {1}. -> УДАР! ',
        rare: str = 'обычная', #редкость брони
    ):
        super().__init__(name, description, use_text, rare)
        self.damage = damage
        self.crit_damage = crit_damage
        self.crit_chance = crit_chance
        self.places_to_hit_and_their_chance = places_to_hit_and_their_chance
       

    def print_info_about_item(self):
        super().print_info_about_item()

        print('Редкость оружия:', self.rare)
        print('Уровень урона:', self.damage)
        print('Шанс критического урона:', self.crit_chance)


    def use(self, who_use: Character, target: Character, place_to_hit):  # target - цель
        if self.crit_chance >= random():
            damage = (self.crit_damage + randint(-3, 5))*self.dict_rare[self.rare] + who_use.damage_allowance#Подправить потом разброс крит.урона
        else:
            damage = self.damage*self.dict_rare[self.rare] + who_use.damage_allowance

        print(
            self.use_text.format(who_use.name, self.name)
        )
        if self.places_to_hit_and_their_chance[place_to_hit]() == 1:
            target.armor_used.use(self, who_use, target, damage)

        else:
            print(who_use.name, 'промахнулся, хнык-хнык\n')