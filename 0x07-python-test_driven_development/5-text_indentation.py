#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    new =""
    chars = ['.', '?', ':']
    for i in text:
        new += i
        if i in chars:
            new +="\n\n"
    print(new, end="")
