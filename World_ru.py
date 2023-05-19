from Classes.Item import Item
from Classes.Artifact import Artifact
from Classes.Consumable import Consumable
from Classes.Weapon import Weapon
from Classes.Armor import Armor
from Classes.Character import Character
from Classes.Hero import Hero
from Classes.Enemy import Enemy
from Logic_ru import *
from time import sleep


def prologue():
    Richard = Hero('Ричард', 25)
    Richard.weapon_used = Weapon('Ладной меч', 7, 12, 0.2)
    Richard.armor_used = Armor('Ладные доспехи', 15)
    Richard.bow_used = Weapon('Ладной меч', 30, 20, 0.7)
    Richard.consumble_list = [Consumable('Сжечь кого-то', 'Уухухуух', 'Летит зелье', 'негативные эффекты', ['Горение', 5, 2]),                          
    Consumable('Здоровье', 'Пон', 'Летит ракетка баллистическая', 'здоровье', 10), 
    Consumable('Опыт', 'вот да', 'Получил опыта', 'опыт', 15)]
    Richard.create_level_list()
    Richard.artifact_list = [
        Artifact('Ожерелье', 'Ожерелье', '', 'Ура', 'обычная', 'урон', 5)
    ]
    Goblin = Enemy('Гоблин', 10, Armor('Ладные доспехи', 10), Weapon('Ладной меч', 5, 10, 0.1))
    Barbarian = Enemy('Варвар', 25, Armor('Ладные доспехи', 20), Weapon('Ладной меч', 8, 13, 0.2))
    Hell_Boss = Enemy('АДский босс', 60, Armor('Ладные доспехи', 30), Weapon('Ладной меч', 15, 15, 0.4))
    print('Здравствуй, путник, рад приветствовать тебя в рпг, ага-ага, тут должно быть что то ещё, но это не сделали')
    sleep(5)
    print('Рад приветствовать тебя на какой то очень ранней версии игры, а также на обучение, которое и является всей игрой')
    sleep(5)
    print('Сначала сразись с гоблином. Все предметы для боя были выданы тебе, следуй инструкциям и сражайся')
    sleep(5)
    Richard.fight(Goblin)
    if Richard.check_live:
        print('Молодец, ты победил. Как насчет прогуляться до адского замка?')
        sleep(2)
        print('*Идут по деревне*')
        sleep(5)
        print('*Вдруг вылетает варвар*.',
              'Ты должен сразиться с варвыром и одолеть его')
        sleep(5)
        Richard.fight(Barbarian)
        if Richard.check_live:
            print('Молодец, ты одолел варвара. Теперь нам никто не помешает добраться до адского замка')
            sleep(5)
            print('Спрашиваешь зачем мы туда идём? Там находиться огромный монстр и ты должен одолеть его(жуткий сюжет)')
            sleep(5)
            print('*Приходят к адскому замку*',
                  'Ты должен зайти туда и од... *появляется адский монстр и сшибает рассказчика*')
            sleep(5)
            print('"Посмотрим чего ты стоишь, путник."')
            sleep(3)
            Richard.fight(Hell_Boss)
            if Richard.check_live:
                print('Ты герой!!! Ты смог одолеть его, теперь наш мир свободен и будет счастлив, ты достоин звания королевского рыцаря. Отправляйся в новые путешествия, ты теперь справишься сам')
    if not(Richard.check_live):
        print('Ты погиб, путник. Попробуй снова')
    print('The END')
            

prologue()