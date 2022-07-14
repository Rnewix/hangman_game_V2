from random import choice 
import os

def screen():
    pass

def game_over():
    pass

def change_word(old_word, letter, letter_index):
    new_word = list(last_word)
    new_word[letter_index] = letter
    new_word = ''.join(new_word)
    return new_word

def choose_word():
    pass 

def score():
    pass

def read_list():
    pass 

def bootgame():
    gametype = input("Please, choose which tipe of game you want to play:\n Animales = 1\n Familiy = 2\n Food = 3")
    while life > 0:
    
        game_over()


points = 0
attemps = 0
life = 0



if __name__ == '__main__':
    bootgame()