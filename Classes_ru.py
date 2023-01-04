from random import randint, random
from time import * 
import sys
from typing import Any


sys.stdout.reconfigure(encoding='utf-8')
'''
Снести если не потребуется функцию bow_shot
'''


class Character: 
    def __init__(
        self, 
        name: str, #Имя героя
        health: int, #Здоровье персонажа
        armor_list: list = list(), #список брони
        weapon_list: list = list(), #список оружия
        consumable_list: list = list() #список зелей
    ): #Фикси, либо делай независимые классы(Я про все предметы инвентаря)/другие названия
        self.name = name 
        self.health = health 
        self.armor_list = armor_list
        self.weapon_list = weapon_list
        self.consumble_list = consumable_list
 
    def strike(self, enemy):
        hit = randint(self.power-10, self.power+10) 
        print( 
        '-> УДАР! ' + self.name + ' атакует ' + enemy.name + 
        'а с силой ' + str(hit) + ', используя ' + self.weapon + '\n') 
 
 
        enemy.armor -= hit 
        if enemy.armor < 0: 
            enemy.health += enemy.armor
            enemy.armor = 0
            if enemy.health < 0:
                enemy.health = 0

            print(
                enemy.name + ' покачнулся.\nКласс его брони упал до '
                + str(enemy.armor) + ', а уровень здоровья до: '
                + str(enemy.health) + '\n')
    
    def bow_shot(self, enemy):
        hit = randint(self.power-5, self.power+5) 
        print( 
        '-> ВЫСТРЕЛ! ' + self.name + ' стреляет ' + enemy.name + 
        'а с силой ' + str(hit) + ', используя ' + self.weapon + '\n') 


        enemy.armor -= hit 
        if enemy.armor < 0: 
            enemy.health += enemy.armor
            enemy.armor = 0

            print(
                enemy.name + ' покачнулся.\nКласс его брони упал до '
                + str(enemy.armor) + ', а уровень здоровья до: '
                + str(enemy.health) + '\n')

    def add_item_to_inventory(self, type_to_item, item):
        if type_to_item == 'оружие':
            self.weapon_list.append(item)
        if type_to_item == 'броня':
            self.armor_list.append(item)
        if type_to_item == 'зелье':
            self.consumble_list.append(item)

    def inventory(self, purpose_work_with_inventory):#вторая переменная - цель работы
        if purpose_work_with_inventory == 'информация':
            print('Инвентарь - покажет весь ваш инвентарь')
            print('Основной предмет - вы сможете поставить броню/оружие как основное для использования в боях')
        elif purpose_work_with_inventory == 'инвентарь':
            print('Вся броня в вашем инвентаре:', ', '.join([x.name for x in self.armor_list]))
            print('Всё оружие в вашем инвентаре:', ', '.join([x.name for x in self.weapon_list]))
            print('Все зелья в вашем инвентаре:', ', '.join([x.name for x in self.consumble_list]))
        elif purpose_work_with_inventory == 'основной предмет':
            Choosing_what_type_of_item = input('Какой тип предмета вы хотите поставить на использование?(броня/оружие)').lower()
            while Choosing_what_type_of_item != 'броня' and 'оружие':
                Choosing_what_type_of_item = input('Что то не совпадает, попробуй ещё раз. Какой тип предмета вы хотите поставить на использование?(броня/оружие)').lower()

            if Choosing_what_type_of_item == 'броня':
                bow_or_melee_weapon = input('Лук или оружие ближнего боя?').lower()
                while bow_or_melee_weapon != 'лук' and 'оружие ближнего боя':
                    bow_or_melee_weapon = input('Что то не совпадает, попробуй ещё раз. Лук или оружие ближнего боя?').lower()
                self.armor_used = input('Выберите броню которую будете использовать:', ', '.join([x.name for x in self.armor_list]))
            elif Choosing_what_type_of_item == 'оружие':
                self.weapon_used = input('Выберите оружие которое будете использовать:', ', '.join([x.name for x in self.weapon_list]))
        #ещё назначения
 
#Нужен ли этот класс, тогда менять впринципе под злодея
class Goblin(Character):
    def __init__(
        self, 
        name: str, #Имя героя
        health: int, #Здоровье персонажа
        armor_list: list = list(), #список брони
        weapon_list: list = list(), #список оружия
        consumable_list: list = list() #список зелей
    ):
        super().__init__(name, health, armor_list, weapon_list, consumable_list)  
 
class Hero(Character):
    def __init__(
        self, 
        name: str, #Имя героя
        health: int, #Здоровье персонажа
        level: int, #Уровень персонажа
        xp: int, #Количество опыта персонажа
        check_live: bool, #Жив ли персонаж или нет
        armor_list: list = list(), #список брони
        weapon_list: list = list(), #список оружия
        consumable_list: list = list() #список зелей
    ):
        super().__init__(name, health, armor_list, weapon_list, consumable_list)
        self.xp = xp
        self.level = level
        self.check_live = check_live#это мб на снос
 
    def print_info(self):#Мб подправить в будущем
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья:', self.health)
        print('Уровень персонажа:', self.level)
    
'''
class Inventory:
    
    def __init__(self):#Создаём чисто списки где будут хранится вещи инвентаря
        
        self.weapons = list()
        self.player_armors = list()
        self.player_potions = list()
        self.player_items = list()
    
    def adding_to_inventory(self, what_is_the_subject, The_name_of_the_object_for_inventory):
        
        variations_of_items_for_inventory = {
            'Оружие': self.weapons.append(The_name_of_the_object_for_inventory),
            'Броня': self.player_armors.append(The_name_of_the_object_for_inventory),
            'Зелье': self.player_potions.append(The_name_of_the_object_for_inventory),
            'Предмет': self.player_items.append(The_name_of_the_object_for_inventory)
        }

        variations_of_items_for_inventory[what_is_the_subject]

    def print_inventory(self):
        print(self.weapons, self.player_armors, self.player_potions, self.player_items)
        '''

class Item:
    def __init__(
        self,
        name: str,  # Название предмета
        description: str = '',  # Описание предмета
        use_text: str = 'Этот предмет красивый',
    ):
        self.name = name
        self.description = description
        self.use_text = use_text

    def print_info_about_item(self):
        print(self.description)

    def use(self):
        print(self.use_text)


class Consumable(Item):
    def __init__(
        self,
        name: str,  # Название предмета
        description: str = '',  # Описание предмета
        use_text: str = 'Это лучше не пить...',
        attribute: str = None,  # Какой-либо атрибут, который будет меняться при использовании предмета
        value: Any = None,  # Значение на которое будет меняться выбранный атрибут
    ):
        super().__init__(name, description, use_text)
        self.attribute = attribute
        self.value = value

    def use(self, who_use: Hero):
        super().use()

        # Если значение не задано, то сразу выходим из функции
        if self.value is None:
            return

        if self.attribute == 'health':
            who_use.health += self.value
        elif self.attribute == 'xp':  # Зелька опыта, например
            who_use.get_xp(self.value)
        elif self.attribute == 'Сам придумай что-нибудь :3':
            # who_use.какой_то_атрибут = self.value
            pass

class Weapon(Item):
    def __init__(
        self,
        name: str,  # Название предмета
        damage: int,  # Урон
        crit_damage: int,  # Критический урон
        crit_chance: float,  # Шанс крита: от 0 и до 1. 0.5 = 50%, 0.2 = 20% и т.д.
        description: str = '',  # Описание предмета
        use_text: str = '-> УДАР! {0} атакует {1} с силой {2}, используя {3}.',
    ):
        super().__init__(name, description, use_text)
        self.damage = damage
        self.crit_damage = crit_damage
        self.crit_chance = crit_chance

    def use(self, who_use: Character, target: Character):  # target - цель
        if self.crit_chance >= random():
            damage = self.crit_damage + randint(-5, 10)#Подправить потом разброс крит.урона
        else:
            damage = self.damage

        print(
            self.use_text.format(who_use.name, target.name, damage, self.name)
        )

'''
Делаем небольшой рандом в изменение процента защиты, ситуации для лука/оружия ближнего боя
'''
class Armor(Item):
    def __init__(self,
        name: str,  # Название предмета
        damage_reduction_percentage: int, #Процент снижения урона от атаки
        description: str = 'Защищает вас',  # Описание предмета
        use_text: str = 'Наносится удар по броне'
    ):
        super().__init__(name, description, use_text)
        self.damage_reduction_percentage = damage_reduction_percentage
    
    def use(self, What_beats: Weapon):
        super().use()

        What_beats.damage -= What_beats.damage * (self.damage_reduction_percentage/100)
    #снести все нафиг наверное, проработать трудную систему с надеванием брони/оружия
