import sys
from Classes.Item import Item
from Classes.Character import Character
from typing import Any


sys.stdout.reconfigure(encoding='utf-8')


class Consumable(Item):
    def __init__(
        self,
        name: str,  # Название предмета
        description: str = '',  # Описание предмета
        use_text: str = 'Это лучше не пить...',
        attribute: str = None,  # Какой-либо атрибут, который будет меняться при использовании предмета
        value: Any = None,  # Значение на которое будет меняться выбранный атрибутб
        rare: str = 'обычная',
    ):
        super().__init__(name, description, use_text, rare)
        self.attribute = attribute
        self.value = value


    def print_info_about_item(self):
        super().print_info_about_item()

        print('Редкость зелья:')
        print('Атрибут зелья:', self.attribute)


    def use(self, who_use: Character, target: Character = None):
        super().use()
    

        # Если значение не задано, то сразу выходим из функции
        if self.value is None:
            return

        if self.attribute == 'здоровье':
            who_use.health += self.value*self.dict_rare[self.rare]
            if who_use.health > who_use.health_limit:
                who_use.health = who_use.health_limit
                print(who_use.name, 'Польностью восстановил здоровье')
            print(who_use.name, 'Восстановил здоровье до', who_use.health)
        elif self.attribute == 'опыт':  # Зелька опыта, например
            who_use.xp += self.value*self.dict_rare[self.rare]
        elif self.attribute == 'негативные эффекты':
            if target in None:
                print('Вы получаете урон, из-за эффекта:', self.value[0])
                who_use.health -= self.value[2]*self.dict_rare[self.rare]
            else:
                target.add_effect(self.value[0], self.value[1], self.value[2]*self.dict_rare[self.rare])
