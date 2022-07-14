from random import choice 
import os

def read_list(type_game):
    file_type = {1:"animals.txt", 2:"family.txt", 3:"food.txt" }
    file_selected = file_type[type_game]
    with open(file_selected, 'r') as f:
        game_word_tuple =  f.readline()
        game_word_tuple = tuple(map(lambda x: x.replace('\n', ''), game_word_tuple))
    return game_word_tuple

def change_word(old_word, letter, letter_index):
    new_word = list(old_word)
    new_word[letter_index] = letter
    new_word = ''.join(new_word)
    return new_word


def screen(screen_type, life, points, word_line, msj):
    game_screens = {99:'screen_title.txt', 98:'screen_game_over.txt', 1:'hang_1.txt', 2:'hang_2.txt', 3:'hang_3.txt', 4:'hang_4.txt', 5:'hang_5.txt', 6:'hang_6.txt', 7:'hang_7.txt', 8:'hang_8.txt', 9:'hang_9.txt'}
    game_screen_display = game_screens[screen_type]
    screen_settings = {'??':str(life), '$$':str(points), '>>':word_line, '<<':msj}
    with open(game_screen_display, 'r') as f:
        screen_displaying =  f.read()
        screen_displaying = str(map(lambda x,y: screen_displaying.replace(x,y), screen_settings))
    return screen_displaying


def game_over():
    pass


def choose_word():
    pass 





def bootgame():
    
    while life > 0:
        print(screen())
        #selected ramdom/make word to figure out
        
        #screen 1
        #choose words
        # if good 
        #   -same screen, appear letter,
        #   choose word
        #if bad
        #   next screem
                #minus points
        #   choose word
        gametype = input()

    # retry screen
    #if yes 
        #life points +1
        # bootgame():
    #elif no        
        #game_over()


points = 0
attemps = 0
life = 3
screen_type = 99



if __name__ == '__main__':
    bootgame()