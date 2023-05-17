from random import randint, random, choice
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
        level: int = 1, #уровень персонажа
        armor_list: list = list(), #список брони
        weapon_list: list = list(), #список оружия
        consumable_list: list = list(), #список зелей
        bow_list: list = list(), #список луков
        artifact_list: list = list(), #различные предметы с баффами
    ):
        self.name = name 
        self.health = health 
        self.health_limit = health
        self.effects = list()
        self.level = level
        self.armor_list = armor_list
        self.weapon_list = weapon_list
        self.consumble_list = consumable_list
        self.bow_list = bow_list
        self.artifact_list = artifact_list
        self.damage_allowance = 0
        self.armor_allowance = 0
    

    def update(self, enemy):#второе - это враг
        deleteEffects = list()
        for i in range(len(self.effects)):
            name, time, level = self.effects[i]
            if name in ['Горение', 'Яд']:
                self.health -= level
                print(self.name, 'получает урон от эффекта', self.effects[i])
            elif name == 'Исцеление':
                self.health += level
                print(self.name, 'восстанавливает здоровье')
                if self.health > self.health_limit:
                    print(self.name, 'восстановил всё здоровье')
                    self.health = self.health_limit
                    time = 0
            time -= 1
            if time <= 0:
                deleteEffects.append(self.effects[i])
            
        for effect in deleteEffects:
            self.effects.remove(effect)


    def add_effect(self, name, time, level):
        for i in range(len(self.effects)):
            if self.effects[i][0] == name:
                self.effects[i][1] += time
                self.effects[i][2] += max(self.effects[i][2], level)
                break
            else:
                self.effects.append([name, time, level])


    def strike(self, enemy, damage, weapon):
        print( 
        self.name + ' атакует ' + enemy.name + 
        'а с силой ' + str(damage) + ', используя ' + weapon.name + '\n') 

        enemy.health -= damage
 
        if enemy.health < 0:
            enemy.health = 0

            print(
                enemy.name + ' покачнулся. Уровень здоровья опустился до: '
                + str(enemy.health) + '\n')

 
#Нужен ли этот класс, тогда менять впринципе под злодея
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
 

class Hero(Character):
    def __init__(
        self, 
        name: str, #Имя героя
        health: int, #Здоровье персонажа
        xp: int = 0, #Количество опыта персонажа
        check_live: bool = True, #Жив ли персонаж или нет
        level: int = 1, #Уровень персонажа
        armor_list: list = list(), #список брони
        weapon_list: list = list(), #список оружия
        consumable_list: list = list(), #список зелей
        bow_list: list = list(), #список луков
        artifact_list: list = list(), #различные предметы с баффами
        artifact_used: list = list(), #может быть объединить в классе Character и нужен ли вообще
    ):
        super().__init__(name, health, level, armor_list, weapon_list, consumable_list, bow_list, artifact_list,)
        self.xp = xp
        self.check_live = check_live
        self.artifact_used = artifact_used
    

    def fight(self, enemy: Enemy):
        while enemy.health and self.health > 0:
            the_thing_to_hit = input('Чем вы предпочтёте воспользоватся(Холодное оружие/Дальнобойное оружие/Зелье): ').lower()
            while the_thing_to_hit not in ['холодное оружие', 'холодное', 'дальнобойное', 'дальнобойное оружие', 'зелье']:
                the_thing_to_hit = input('Что то неправильно. Чем вы предпочтёте воспользоватся(Холодное оружие/Дальнобойное оружие/Зелье): ').lower()
            if the_thing_to_hit in ['холодное оружие', 'холодное', 'дальнобойное оружие', 'дальнобойное']:
                place_to_hit = input('Выберите место удара:(Голова/Туловище/Руки/Ноги): ').lower()
                while place_to_hit not in ['голова', 'туловище', 'руки', 'ноги']:
                    place_to_hit = input('Неправильно. Выберите место удара:(Голова/Туловище/Руки/Ноги)').lower()
            if the_thing_to_hit in ['холодное оружие', 'холодное']:
                self.weapon_used.use(self, enemy, place_to_hit)
            elif the_thing_to_hit in ['дальнобойное оружие', 'дальнобойное']:
                self.bow_used.use(self, enemy, place_to_hit)
            else:
                consumble_used = input(f"Выберите зелье которое будете использовать: {', '.join([x.name for x in self.consumble_list])} ").lower()
                while True:
                        if consumble_used in self.consumble_list:
                            consumble_used.use(self, enemy)
                            break
                        consumble_used = input(f"Выберите зелье которое будете использовать: {', '.join([x.name for x in self.consumble_list])} ").lower()
                
            enemy.update(self)
            if enemy.health <= 0:
                print(enemy.name, 'пал в этом нелёгком бою\n')
                self.restoring_health(enemy)
                self.get_xp('бой', enemy)
                self.new_level()
                self.drop(enemy)
                break
            sleep(5)


            """if (enemy.bow_used is None):
                enemy.bow_used.use(enemy, self, choice(['голова', 'туловище', 'руки', 'ноги']))"""
            enemy.weapon_used.use(enemy, self, choice(['голова', 'туловище', 'руки', 'ноги']))

            self.update(enemy)
            if self.health <= 0:
                print(self.name, ', ваш герой увы пал...\nGameOver')
                self.check_live = False
            sleep(3)


    def print_info(self):#Мб подправить в будущем
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья:', self.health)
        print('Уровень персонажа:', self.level)
        print('Количество опыта:', self.xp)
    

    def drop(self, enemy: Enemy):
        self.weapon_list.append(enemy.weapon_used)
        self.armor_list.append(enemy.armor_used)
        self.bow_list.append(enemy.bow_used)
        self.consumble_list.append(enemy.consumble_used)


    def restoring_health(self, enemy: Enemy):
        self.health += (enemy.health_limit//enemy.weapon_used.damage) * enemy.level#пофиксить формулу если надо
        if self.health > self.health_limit:
            self.health = self.health_limit
        print('Ваше здоровье восстановлено до:', self.health)
    

    def get_xp(self, value, enemy: Enemy):#Нужна ли эта функция
        if value == 'бой':
            self.xp += (enemy.health_limit//enemy.weapon_used.damage) * enemy.level#пофиксить формулу если надо


    def create_level_list(self):
        self.level_list = list()
        q = 1.2
        for i in range(100):
            self.level_list.append(round(10 * (1 - q**5) / (1 - q)))
            q += 0.05


    def new_level(self):
        if self.xp >= self.level_list[self.level]:
            self.level += 1
            self.health_limit += 10
            self.health = self.health_limit
            print(
            'У вас новый уровень. Господа, встречайте рыцаря средиземья с', 
            self.level, 'уровнем\n')


    def add_item_to_inventory(self, type_to_item, item):
        if type_to_item == 'холодное оружие':
            self.weapon_list.append(item)
        elif type_to_item == 'дальнобойное оружие':
            self.bow_list.append(item)
        elif type_to_item == 'броня':
            self.armor_list.append(item)
        elif type_to_item == 'зелье':
            self.consumble_list.append(item)
        

    def inventory(self, purpose_work_with_inventory):#вторая переменная - цель работы
        
        if purpose_work_with_inventory == 'информация':
            print('Предметы - покажет весь ваш инвентарь')
            print('Основной предмет - вы сможете поставить броню/оружие как основное для использования в боях')
        
        elif purpose_work_with_inventory == 'предметы':
            print('Вся броня в вашем инвентаре:', ', '.join([x.name for x in self.armor_list]))
            print('Всё холодное оружие в вашем инвентаре:', ', '.join([x.name for x in self.weapon_list]))
            print('Всё дальнобойное оружие в вашем инвентаре:', ', '.join([x.name for x in self.bow_list]))
            print('Все зелья в вашем инвентаре:', ', '.join([x.name for x in self.consumble_list]))
        
        elif purpose_work_with_inventory == 'добавление в использование':
            Choosing_what_type_of_item = input('Какой тип предмета вы хотите поставить на использование?(броня/оружие/артефакты): ').lower()
            while Choosing_what_type_of_item not in ['броня', 'оружие', 'артефакт', 'артефакты']:
                Choosing_what_type_of_item = input('Что то не совпадает, попробуй ещё раз. Какой тип предмета вы хотите поставить на использование?(броня/оружие/артефакты): ').lower()
            if Choosing_what_type_of_item == 'броня':
                armor_list = [item.name.lower() for item in self.armor_list]
                self.armor_used = input(f"Выберите броню которую будете использовать: {', '.join([x.name for x in self.armor_list])} ")
                while True:
                        if self.armor_used.lower() in armor_list:
                            self.armor_used = self.armor_list[armor_list.index(self.armor_used)]
                            break
                        self.armor_used = input(f"Что то неправильно. Выберите броню которую будете использовать: {', '.join([x.name for x in self.armor_list])} ")
            
            elif Choosing_what_type_of_item == 'оружие':
                bow_or_melee_weapon = input('Дальнобойное или холодное оружие?').lower()
                while bow_or_melee_weapon != 'дальнобойное оружие' and 'холодной оружие' and 'дальнобойное' and 'холодное':
                    bow_or_melee_weapon = input('Что то не совпадает, попробуй ещё раз. Лук или оружие ближнего боя?').lower()                 
                
                if bow_or_melee_weapon == 'холодное оружие' and 'холодное':
                    weapon_list = [item.name.lower() for item in self.weapon_list]
                    self.weapon_used = input(f"Выберите оружие которое будете использовать: {', '.join([x.name for x in self.weapon_list])} ", )
                    while True:
                        if self.weapon_used.lower() in weapon_list:
                            self.weapon_used = self.weapon_list[weapon_list.index(self.weapon_used)]
                            break
                        self.weapon_used = input(f"Что то неправильно. Выберите оружие которое будете использовать: {', '.join([x.name for x in self.weapon_list])} ", )
                
                else:
                    bow_list = [item.name.lower() for item in self.bow_list]
                    self.bow_used = input(f"Выберите дальнобойное оружие которое будете использовать:{', '.join([x.name for x in self.bow_list])} ", )
                    while True:
                        if self.bow_used.lower() in bow_list:
                            self.bow_used = self.bow_list[bow_list.index(self.bow_used)]
                            break
                        self.bow_used = input(f"Что то неправильно. Выберите дальнобойное оружие которое будете использовать:{', '.join([x.name for x in self.bow_list])} ", )         

            elif Choosing_what_type_of_item == 'артефакт' or Choosing_what_type_of_item == 'артефакты':
                if len(self.artifact_used) < 3:
                    artifact_list = [item.name.lower() for item in self.artifact_list]
                    artifact_used = input(f"Выберите артефакт который будете использовать: {', '.join([x.name for x in self.artifact_list])} ", )
                    while True:
                        if artifact_used.lower() in artifact_list:
                            self.artifact_used.append(self.artifact_list[artifact_list.index(artifact_used)])
                            artifact_used.use(self, True)
                            break
                        artifact_used = input(f"Что то неправильно. Выберите артефакт который будете использовать: {', '.join([x.name for x in self.artifact_list])} ", )
    
        elif purpose_work_with_inventory == 'снятие с использования':
            Choosing_what_type_of_item = input('Какой тип предмета вы хотите снять с использования?(броня/оружие/артефакты): ').lower()
            while Choosing_what_type_of_item not in ['броня', 'оружие', 'артефакт', 'артефакты']:
                Choosing_what_type_of_item = input('Что то не совпадает, попробуй ещё раз. Какой тип предмета вы хотите снять с использования?(броня/оружие/артефакты): ').lower()
            
            if Choosing_what_type_of_item == 'артефакт':#сделать цикл, чтобы человек мог убрать несколько артефактов
                artifact_list = [item.name.lower() for item in self.artifact_used]
                artifact_unused = input(f"Выберите артефакт который хотите снять: {', '.join([x.name for x in self.artifact_used])} ", )
                while True:
                        if artifact_unused.lower() in artifact_used:
                            artifact_unused = self.artifact_used[artifact_used.index(artifact_unused)]
                            self.artifact_used.remove(artifact_unused)
                            artifact_used.use(self, False)
                            break
                        artifact_unused = input(f"Выберите артефакт который хотите снять: {', '.join([x.name for x in self.artifact_used])} ", )


class Item:
    def __init__(
        self,
        name: str,  # Название предмета
        description: str = '',  # Описание предмета
        use_text: str = 'Этот предмет красивый',
        rare: str = 'обычная',
    ):
        self.name = name
        self.description = description
        self.use_text = use_text
        self.rare = rare
        self.dict_rare = {
            'обычная': 1,
            'необычная': 1.1,
            'редкая': 1.3,
            'эпическая': 1.6,
            'легендарная': 1.8,
            'мифическая': 2
        }#бафы редкостей, потом изменить проценты


    def print_info_about_item(self):
        print('Имя предмета:', self.name)
        print(self.description)


    def use(self):
        print(self.use_text)

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

    #мб чето добавить для брони