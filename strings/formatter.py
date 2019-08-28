###
### Author: Mikaeri Ohana
### Date: 8/27/2019
###

import sys
import os
import re

param_original_text_path = sys.argv[1]
param_limit = int(sys.argv[2])
param_justify = str(sys.argv[3]).lower()

def main():
    text = open_file(param_original_text_path)
    text = limiter(text, param_limit)
    if param_justify == 'true':
        text = justify(text, param_limit)
    path = create_file(str(text))
    print("Your file is ready in the folder: " + path)

def open_file(path):
    with open(path, "r") as file:
        return file.read()

def limiter(text, limit):
    fulltext = ''
    line = ''
    word = ''
    for char in text:
        if char != " " and char != "\n":
            word += char

        if char == " " or char == "\n":
            if len(line) + len(word) <= limit - len(char):  
                line = line + ' ' + word if len(line) > 0 else word
                word = ''                
            else:
                fulltext += line + '\n'
                line = word
                word = ''
		
            if char == '\n':
                fulltext +=  line + '\n'
                line = ''
        
    return fulltext

def justify(text, limit):
    sentences = text.split('\n')
    fulltext = ''

    for sentence in sentences:
            if sentence == '':
                fulltext += '\n'
            else:
                vector = re.split("( )", sentence)   
                len_sentence = len(sentence)
                for word in vector:
                        if len_sentence < limit:
                            word += ' '                            
                            len_sentence+=1
                        fulltext += word
                fulltext += '\n'

    return fulltext

def create_file(text):
        path = ""
        i = 1
        while os.path.exists("result-text%s.txt" % i):
                i += 1
                
        with open("result-text%s.txt" % i, "w") as file:
                file.write(text)
                file.close()
                path = "result-text%s.txt" % i
        return path

if __name__ == "__main__":
	main()