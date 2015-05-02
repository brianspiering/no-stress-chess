#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Create eletronic version of No Stress Chess®

Video demo - https://www.youtube.com/watch?v=Vn0bMld-K9w

Since it removes strategry and "tranny of choice", 
it is a great way to learn chess.

Level 1:
Randomly pick from "a card" that contains a chess piece. 
If the person is able to move the piece, move the piece.
If the person is unable to move the pice, pick another card.
Then the next person takes a turn.

Level 2:
Pick a card from your hand of 5 cards.
"""

import os
from random import choice

pieces = {'King': 'Moves exactly one vacant square in any direction: forwards, backwards, left, right, or diagonally',
        'Queen': 'Moves any number of vacant squares in any direction: forwards, backwards, left, right, or diagonally, in a straight line.',
        'Rook': 'Moves any number of vacant squares forwards, backwards, left, or right in a straight line.',
        'Bishop': 'Moves any number of vacant squares diagonally in a straight line.',
        'Knight': 'Moves on an extended diagonal from one corner of any 2×3 rectangle of squares to the furthest opposite corner.',
        'Pawn': "Moves forward exactly one space. Optionally, two spaces when on its starting square, toward the opponent's side of the board. When there is an enemy piece one square diagonally ahead of the pawn, either left or right, then the pawn may capture that piece."}

cards = None # 56 action cards

def play():
    while True:
        i = input("Press enter to get piece (or q to quit): ")
        if i != 'q':
            current_piece = choice(list(pieces.keys()))
            # print(os.system('clear'))
            os.system('cls' if os.name == 'nt' else 'clear')
            # print(chr(27) + "[2J")
            print(current_piece, '\n')
            print(pieces[current_piece], '\n')
        else:
            break

    print("Thanks for trying playing No Stress Chess® ")

if __name__ == '__main__':
    play()