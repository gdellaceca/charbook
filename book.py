"""Book.py
	The program reads a text file and counts the occurrence of each letter of 
    the alphabet.
	"""
	
import argparse  #To parse console arguments
#import os.path multiplatform
#letters ="abcdefghijklmnopqrstuvwxyz"
import time
import math

def histogram(d:dict):
    for i in d:
        h= math.floor(d[i])*"*"
        print(f"{i}|{h} |{d[i]:.2f}")


parse= argparse.ArgumentParser(description= "A program that prints the relative \
                               frequency of the letters contained in a .txt file") #create object ArgumentParser
parse.add_argument("book", help = "The .txt file", default = "pg1497.txt")
parse.add_argument("-hi", help = "Shows a histogram of the frequencies", action="store_true")
args= parse.parse_args() #use object method

letters = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
n = 0

f = open(args.book,encoding="utf8")
text = f.read()
f.close()
start = time.perf_counter()

for i in text.lower():
    n += 1
    for l in list(letters):
        if i == l:
            letters[i] += 1

freq= {}

for i in letters:
    freq[i]= letters[i]/n*100
    if not args.hi:
        print(f"{i} : {freq[i]:.2f}%")
    


if args.hi:
    histogram(freq)
else:    
    print(letters)
    
stop = time.perf_counter()
print(f"Elapsed time : {stop-start:.5f} s")
