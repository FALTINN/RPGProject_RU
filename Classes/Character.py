import sys


sys.stdout.reconfigure(encoding='utf-8')


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