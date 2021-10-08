''' charbook.py
The program reads a text file and counts the occurrence of each letter of
    the alphabet.
'''
import time
import argparse
#import os yet to be done
#import logging  yet to be done



def read_book(source:str):

    with open(source,mode='r',encoding='utf-8') as f:
        data = f.read()
        return data



def countchar(l:str): #counts the alphabetic characters in a string
    ab = {key : 0 for key in 'abcdefghijklmnopqrstuvwxyz'}
    numchar = 0

    for i in l:
        numchar += 1
        if i in list(ab):
            ab[i] += 1

    return ab , numchar


def histogram():
    pass

start = time.perf_counter()

parser = argparse.ArgumentParser()
parser.add_argument('book', help = 'The txt file to be used.')
parser.add_argument('-histo', help = 'plot an histogram of the data.\
                    ',action= 'store_true')
parser.add_argument('-stats', help = 'show more useful stats, like number  \
                    of words or number of lines.', action= 'store_true')
args = parser.parse_args()

book = read_book(args.book)

freq, n = countchar(book)

for t in freq:
    print(f'{t} : {freq[t]/n:.4f}')

stop = time.perf_counter()

print(f'Elapsed time: {stop-start} s')
