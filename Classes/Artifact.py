import sys
from Classes.Item import Item
from Classes.Character import Character


sys.stdout.reconfigure(encoding='utf-8')


class Artifact(Item):
    def __init__(
        self,
        name: str,  # Название предмета
        item_type: str,
        description: str = '',  # Описание предмета
        use_text: str = 'Этот предмет красивый',
        rare: str = 'обычная',
        attribute: str = None,  # Какой-либо атрибут, который будет меняться при использовании предмета
        value: int = None,  # Значение на которое будет меняться выбранный атрибутб
    ):
        super().__init__(name, description, use_text, rare)
        self.item_type = item_type
        self.attribute = attribute
        self.value = value


    def use(self, who_use: Character, work: bool = True):#work-добавляем мы или удаляем баффы, True - добавляем, False - убираем
        
        if self.value is None:
            return
        
        elif self.attribute == 'здоровье':
            if work:
                who_use.health_limit += self.value   
            else:
                who_use.health_limit += self.value   
        elif self.attribute == 'урон':
            if work:
                who_use.damage_allowance += self.value
            else:
                who_use.damage_allowance -= self.value
        elif self.attribute == 'защита':
            if work:
                who_use.armor_allowance += self.value
            else:
                who_use.armor_allowance -= self.value