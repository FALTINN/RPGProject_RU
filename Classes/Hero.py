import sys
from Classes.Character import Character
from Classes.Enemy import Enemy
from random import choice
from time import sleep


sys.stdout.reconfigure(encoding='utf-8')


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
