from random import choice 
import os


def read_list(game_mode):
    file_type = {1:"animals.txt", 2:"family.txt", 3:"food.txt" }
    file_selected = file_type[game_mode]
    with open(file_selected, 'r') as f:
        game_word_tuple =  f.readlines()
        game_word_tuple = tuple(map(lambda x: x.replace('\n', ''), game_word_tuple))
    return game_word_tuple


def change_word(old_word, letter, letter_index):
    new_word = list(old_word)
    new_word[letter_index] = letter
    new_word = ''.join(new_word)
    return new_word


def screen(screen_type, life, points, word_line, msj):
    game_screens = {99:'screen_title.txt', 98:'screen_game_over.txt', 97:'screen_victory.txt', 96:'screen_ endgame.txt', 1:'hang_1.txt', 2:'hang_2.txt', 3:'hang_3.txt', 4:'hang_4.txt', 5:'hang_5.txt', 6:'hang_6.txt', 7:'hang_7.txt', 8:'hang_8.txt', 9:'hang_9.txt'}
    game_screen_display = game_screens[screen_type]
    screen_settings = {'??':str(life), '$$':str(points), '>>':word_line, '<<':msj}
    with open(game_screen_display, 'r') as f:
        screen_displaying =  f.read()
    for i, i2 in screen_settings.items():
        screen_displaying = screen_displaying.replace(i, i2)
    return screen_displaying


def retry(life):
    life = life
    retry = 0
    while retry == 0:
        try:
            retry = int(input())
            assert retry == 1 or 2
        except:
            os.system("clear")
            print('Wrong input, select 1 or 2:\n Do you want to try again?\nYES = 1\nNO = 2')
            retry = 0
    if retry == 1:
        screen_type = 99
    elif retry == 2:
        screen_type = 96
        life = 0
    return screen_type, life


def bootgame():
    game_run = True
    life = 3
    points = 0
    screen_type = 0
    game_mode = 0
    figure_out_word = ''
    word_line = ''
    msj = ''
    choose_letter = ''
    used_letters = []
    mistake = ['No', 'Nope', 'Not even close', 'Good try, but nop']
    find_msj = ['Good, you found one', 'Yeah, you are more close to win', 'Found one, continue like this', 'Your election was correct']
    while game_run == True:
        if life > 0:
            screen_type = 99       
            used_letters = []                                 
            os.system("clear")
            print(screen(screen_type, life, points, word_line, msj))
            msj = ''                                                
            try:
                game_mode = int(input())
                assert game_mode == 1 or 2 or 3
            except:
                msj = 'Wrong input, select 1, 2 or 3:'
                continue
            else:
                figure_out_word = choice(read_list(game_mode))
                word_line = '_' * len(figure_out_word)
                screen_type = 1                
            while '_' in word_line and screen_type != 7:   
                os.system("clear")
                print(screen(screen_type, life, points, word_line, msj))
                try:
                    choose_letter = str(input())
                    choose_letter = choose_letter.upper() 
                    assert choose_letter == ('A' <= choose_letter) or (choose_letter <= 'Z') and choose_letter.isalpha()
                except:    
                    choose_letter = ''
                    msj = 'please choose only one letter from A to Z'
                    continue 
                if choose_letter in used_letters:
                    msj = 'Becarefull, you already used that letter'
                    screen_type += 1 
                elif not choose_letter in figure_out_word:
                    used_letters.append(choose_letter)
                    msj = choice(mistake) + ', try again'
                    screen_type += 1
                else:
                    used_letters.append(choose_letter)
                    while choose_letter in figure_out_word:
                        letter_index = figure_out_word.find(choose_letter)
                        word_line = change_word(word_line, choose_letter, letter_index)
                        figure_out_word = change_word(figure_out_word, '*', letter_index)
                        msj = choice(find_msj)
            if '_' not in word_line:
                points += 1
                msj = ''
                screen_type = 97
                os.system("clear")
                print(screen(screen_type, life, points, word_line, msj))
                screen_type, life = retry(life)
            elif screen_type == 7 and life >1:
                life -=1 
                msj = ''
                screen_type = 98                                        
                os.system("clear")
                print(screen(screen_type, life, points, word_line, msj))
                screen_type, life = retry(life)
            elif screen_type == 7 and life == 1:
                life -=1 
        elif life == 0:
            screen_type = 96                                        
            os.system("clear")
            print(screen(screen_type, life, points, word_line, msj))
            game_run = False
                

if __name__ == '__main__':
    bootgame()