from random import randint
from Classes_ru import *
import sys

sys.stdout.reconfigure(encoding='utf-8')

#SQL, сохранения и акки, имба
def login():
    pass

def registration():
    pass


def hit_the_spot(place_of_impact, the_thing_to_hit, which_beats: Hero, who_is_being_beaten: Character):#поменять потом к каким классам отсылает
    
    places_to_hit_and_their_chance = {
        'лук': {
            'голова': randint(1, 8),
            'туловище': randint(1, 3),
            'руки': randint(1, 6),
            'ноги': randint(1, 5)
        },
        'меч': {
            'голова': randint(1, 5),
            'туловище': randint(1, 1.5),
            'руки': randint(1, 3),
            'ноги': randint(1, 3)
        }
    }#Вырубай генератор рандомных чисел

    print('\nВы целитесь в', place_of_impact)

    if the_thing_to_hit == 'лук':
        
        if places_to_hit_and_their_chance[the_thing_to_hit][place_of_impact] == 1:
            print('Вы попадаете!')
            which_beats.bow_shot(who_is_being_beaten)

        else:
            print('Вы промахнулись, хнык-хнык')
    
    
    elif the_thing_to_hit == 'меч':
        
        if places_to_hit_and_their_chance[the_thing_to_hit][place_of_impact] == 1:
            print('Вы попадаете!')
            which_beats.strike(who_is_being_beaten)
        
        else:
            print('Вы промахнулись, хнык-хнык')
    

def fight(which_beats: Hero, who_is_being_beaten: Character):#если что, поменять может быть потом к каким классам
    
    while who_is_being_beaten.health and which_beats.health > 0:
        the_thing_to_hit = input('Чем вы предпочтёте ударить: ').lower()#Напоминаю про механики инвентаря и что надо будет делать
        place_of_impact = input('Место удара: ').lower()#Оптимизировать потом
        hit_the_spot(place_of_impact, the_thing_to_hit, which_beats, who_is_being_beaten)
        if who_is_being_beaten.health <= 0:
            print(who_is_being_beaten.name, 'пал в этом нелёгком бою\n')
            which_beats.xp += 50
            break
        sleep(5)

        who_is_being_beaten.strike(which_beats)#Тоже это грамотно оформить
        if which_beats.health <= 0:
            print(which_beats.name, 'Ваш герой увы пал...\nGameOver')
            which_beats.check_live = False
        sleep(3)

    #Оптимизиоравать и подумать о надобности fight, check_live


def New_level(which_get_new_level: Hero):

    level_list = (0, 50, 200, 400, 900, 1500)#мб потом накинуть её в другое место
    
    if which_get_new_level.xp >= level_list[which_get_new_level.level]:
        which_get_new_level.level += 1
        print(
        'У вас новый уровень. Господа, встречайте рыцаря средиземья с', 
        which_get_new_level.level, 'уровнем\n')
 