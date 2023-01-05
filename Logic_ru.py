from random import randint
from Classes_ru import *
import sys

sys.stdout.reconfigure(encoding='utf-8')

#SQL, сохранения и акки, имба
def login():
    pass

def registration():
    pass


def hit_the_spot(place_of_impact, the_thing_to_hit, which_beats: Hero, who_is_being_beaten: Character):#А зачем она нужна, эт оможно в классах реализовать
    
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
    

def New_level(which_get_new_level: Hero):#Да, кинуть функцию в класс Hero

    level_list = (0, 50, 200, 400, 900, 1500)#мб потом накинуть её в другое место
    
    if which_get_new_level.xp >= level_list[which_get_new_level.level]:
        which_get_new_level.level += 1
        print(
        'У вас новый уровень. Господа, встречайте рыцаря средиземья с', 
        which_get_new_level.level, 'уровнем\n')
 