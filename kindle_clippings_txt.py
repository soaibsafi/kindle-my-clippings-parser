# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 19:54:00 2020

@author: Soaib
"""

with open('test/My Clippings.txt', 'r', encoding='utf8' ) as f:
    lines = f.readlines()
book_list = lines[0::5]

books = list()
for line in book_list :
    if line not in books:
        books.append(line)

w = open("test/parsed-clippings1.txt", "a", encoding='utf8')
for book in books:  
    #print(book)
    w.write('## '+book)
    for position, i in enumerate(lines):
        if book in i:
            print(lines[position+3])
            w.write('- '+lines[position+3])
            
w.close()      