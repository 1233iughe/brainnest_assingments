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
        sentences = file.read()
        file.close()
        print(sentences)

