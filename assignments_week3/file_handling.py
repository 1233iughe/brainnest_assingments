"""
1. Write a Python program that reads a text file and prints the number of lines, words, and characters in the file.
2. Write a Python program that reads a CSV file and converts it into a dictionary. Each row of the CSV file should be a key-value pair in the dictionary.
3. Write a Python program that reads a binary file and converts it into a hexadecimal string. The program should output the hexadecimal string to a text file.
4. Write a Python program that reads a text file containing numbers and calculates the sum of all the numbers in the file.
5. Write a Python program that reads a text file and removes all the blank lines. The modified text should be written back to the file.

"""
import os
def info(path):
    if os.path.exists(path):
        file = open(path)
        allfile = file.read()
        file.close()
        lines = str(allfile.count('\n'))
        words = str(len(allfile.split()))
        char = str(len(allfile))
        print("N° of lines: " + lines, "N° of words: " + words, "N° of characters: " + char)

info('./file_handling.txt')

import csv
def csv_dic(path):
    if os.path.exists(path):
        file = open(path)
        rows = csv.reader(file)
        dicto = {f'row{i}':row for i, row in enumerate(rows)}
        file.close()
        return dicto
print(csv_dic('./example.csv'))

def binary_hexa(path):
    if os.path.exists(path):
        file = open(path, 'rb')
        data = file.read().hex()
        file.close()
        file = open("hexa.txt", 'w')
        file.write(data)
        file.close()        
binary_hexa('./file.bin')

def adder(path):
    if os.path.exists(path):
        file = open(path)
        data = file.read().split()
        file.close()
        return sum([int(num) for num in data])
print(adder('./numbers.txt'))

def blanks(path):
    if os.path.exists(path):
        file = open(path,'r+')
        data = file.read().split('\n')
        no_blank = [x for x in data if x]
        new = '\n'.join(no_blank)
        file.seek(0)
        file.write(new)
        file.truncate()
        file.close()

blanks('./blanks.txt')