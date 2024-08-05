import os

def beemaker():
    with open('beescript.txt', 'r') as bs:
        for i in bs:
            print(i)

beemaker()