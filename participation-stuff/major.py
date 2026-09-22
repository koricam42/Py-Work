"""
Program Name: Dice Roll
Author: Jordan Mensah
Purpose: Python-based program rolls a die
Starter Code: 
 - Instructions/General Help: https://learning.oreilly.com/library/view/python-crash-course/9781098156664/c09.xhtml#h1-502703c09-0001
Date: 9/21/26
"""
from random import randint

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    
    def roll_die(self):
        roll = randint(1, self.sides) 
        print(roll)

