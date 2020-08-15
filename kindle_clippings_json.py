# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 00:01:01 2020

@author: Soaib
"""

import json
import re
from typing import List
class Highlights:
    def __init__(self, bookname:str, highlights:str):
        self.bookname = bookname
        self.heighlight = highlights
    
    def reprJSON(self):
        return dict(bookname=self.bookname, highlights=self.heighlight)
        
class Date:
    def __init__(self, date:str, highlights:List[Highlights]):
        self.date = date
        self.highlights = highlights
    
    def reprJSON(self):
        return dict()


with open('test/My Clippings.txt', 'r', encoding='utf8' ) as f:
    lines = f.readlines()

dates = []
temp_dates = []

for i, line in enumerate(lines):
    d = re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December|)\s\d\d\,\s\d{4}', lines[i])
    if(len(d) != 0):
        temp_dates.append(d[0])
        
[dates.append(x) for x in temp_dates if x not in dates]
dates_count = len(dates)

date_list = []
while(dates_count):
    highlight_list = []
    for i, line in enumerate(lines):
        if dates[dates_count-1] in line:
            highlight_list.append(Highlights(lines[i-1], lines[i+2]))
    date_list.append(Date(dates[dates_count-1], highlight_list))
    dates_count -= 1
    
json_data = json.dumps(date_list, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)

with open("test/data_file.json", "w", encoding='utf8') as write_file:
    json.dump(json_data, write_file)






        



