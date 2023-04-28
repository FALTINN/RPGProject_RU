from Classes_ru import *
from Logic_ru import *

def prologue():
    Richard = Hero('Ричард', 35)
    Richard.weapon_used = Weapon('Ладной меч', 10, 15, 0.1)
    Richard.armor_used = Armor('Ладные доспехи', 15)
    Richard.bow_used = Weapon('Ладной меч', 30, 20, 0.7)
    Richard.consumble_list = [Consumable('Сжечь кого-то', 'Уухухуух', 'Летит зелье', 'негативные эффекты', ['Горение', 5, 2]), 
    Consumable('Здоровье', 'Пон', 'Летит ракетка баллистическая', 'здоровье', 10), 
    Consumable('Опыт', 'вот да', 'Получил опыта', 'опыт', 15)]
    Richard.artifact_list = [
        Artifact('Ожерелье', 'Ожерелье', '', 'Ура', 'обычная', 'урон', 5)
    ]
    Richard.inventory('основной предмет')
    Goblin = Enemy('Вен', 20, Armor('Ладные доспехи', 50), Weapon('Ладной меч', 5, 10, 0.1), Weapon('Ладной меч', 30, 20, 0.7))
    Richard.fight(Goblin)

prologue()